#!/usr/bin/env python3
"""Download product images listed in a saved Shopify Admin GraphQL result.

The Shopify data is pulled READ-ONLY through the Shopify connector (no tokens
in this repo). Save the query result as JSON, then:

  python3 fetch_images.py ../data/shopify-hero-media.json --out ../assets/shopify --max 5

Expected JSON shape (Admin GraphQL):
  {"products": {"nodes": [{"handle": "...", "media": {"nodes": [{"image": {"url": "..."}}]}}]}}

Query used (graphql_query, read-only):
  { products(first: 20, query: "handle:a OR handle:b") { nodes { handle title
      media(first: 8) { nodes { ... on MediaImage { image { url width height } } } } } } }

Printify mockups: export/download from Printify (or use the mockup URLs that
Printify pushes to Shopify, which is what the Shopify media URLs already are)
and drop them in assets/printify/<handle>-N.jpg, or reference the URL directly
in a video config ("image": "https://...") and render.py will cache it.
Files are saved as <handle>-<n>.jpg; config refs look like "@assets/shopify/<handle>-1.jpg".
"""
import argparse, json, os, subprocess

ap = argparse.ArgumentParser()
ap.add_argument("json"); ap.add_argument("--out", default="../assets/shopify")
ap.add_argument("--max", type=int, default=5); ap.add_argument("--width", type=int, default=1600)
a = ap.parse_args()
d = json.load(open(a.json))
os.makedirs(a.out, exist_ok=True)
for p in d["products"]["nodes"]:
    for i, m in enumerate([m for m in p["media"]["nodes"] if m][: a.max]):
        url = m["image"]["url"].split("?")[0] + f"?width={a.width}"
        dst = os.path.join(a.out, f"{p['handle']}-{i+1}.jpg")
        if os.path.exists(dst):
            continue
        r = subprocess.run(["curl", "-sf", "--retry", "4", "-o", dst, url])
        print(("ok  " if r.returncode == 0 else "FAIL") + " " + dst)
