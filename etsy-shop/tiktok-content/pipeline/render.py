#!/usr/bin/env python3
"""FurEver Faces TikTok slideshow renderer.

One config (JSON or YAML) in -> one 1080x1920 (9:16) H.264 MP4 out, 7-15 s,
silent (no audio track), with text overlays kept inside TikTok safe zones.

Frames are composed with Pillow (Ken Burns motion, crossfades, text cards)
and piped as raw RGB into ffmpeg for encoding.

Usage:
  python3 render.py configs/2026-11-17-santa-paws-ornament.json
  python3 render.py configs/*.json --qa          # + QA frames + safe-zone previews
  python3 render.py configs/x.json --check       # validate config only

See README.md for the config schema.
"""
import argparse, hashlib, json, os, re, subprocess, sys, urllib.request
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1080, 1920
# TikTok UI-safe region: top tabs (~200px), right action rail (~130px),
# bottom caption/username/music bar (~480px). Keep all text inside this box.
SAFE = dict(left=60, top=210, right=W - 130, bottom=H - 480)   # x 60..950, y 210..1440
MIN_LEN, MAX_LEN = 7.0, 15.0

COLORS = {
    "ink": "#1A1A1A", "cream": "#FFF2DE", "berry": "#C2185B", "berry_dark": "#8B123F",
    "forest": "#1F4D3A", "gold": "#C9A227", "white": "#FFFFFF", "red": "#B23A3A",
}
FONTS = {
    "black": "Poppins-Black.ttf", "xbold": "Poppins-ExtraBold.ttf",
    "bold": "Poppins-Bold.ttf", "semi": "Poppins-SemiBold.ttf",
}
# text styles: font, size, text color, card color (None = outline text), card alpha
STYLES = {
    "hook":  dict(font="black", size=74, color="ink",   card="white", alpha=240, pad=30),
    "body":  dict(font="xbold", size=56, color="ink",   card="white", alpha=230, pad=26),
    "cta":   dict(font="black", size=60, color="cream", card="berry", alpha=250, pad=28),
    "fact":  dict(font="xbold", size=54, color="cream", card="forest", alpha=245, pad=26),
    "small": dict(font="semi",  size=32, color="ink",   card="cream", alpha=225, pad=14),
}
ROOTS = {
    "@design": os.environ.get("FF_DESIGN_ROOT", os.path.join(HERE, "..", "..", "etsy-design")),
    "@assets": os.environ.get("FF_ASSETS_ROOT", os.path.join(HERE, "..", "assets")),
}


def col(c, alpha=255):
    c = COLORS.get(c, c)
    c = c.lstrip("#")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4)) + (alpha,)


def font(name, size):
    return ImageFont.truetype(os.path.join(HERE, "fonts", FONTS[name]), size)


def load_config(path):
    with open(path) as f:
        txt = f.read()
    if path.endswith((".yaml", ".yml")):
        try:
            import yaml
        except ImportError:
            sys.exit("PyYAML not installed; use a .json config or `pip install pyyaml`.")
        return yaml.safe_load(txt)
    return json.loads(txt)


def resolve_image(ref, cfg_dir):
    """Local path, @design/..., @assets/..., or http(s) URL (cached)."""
    if re.match(r"https?://", ref):
        cache = os.path.join(HERE, ".cache")
        os.makedirs(cache, exist_ok=True)
        fn = os.path.join(cache, hashlib.sha1(ref.encode()).hexdigest()[:16] + ".img")
        if not os.path.exists(fn):
            req = urllib.request.Request(ref, headers={"User-Agent": "ff-render/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r, open(fn, "wb") as o:
                o.write(r.read())
        return fn
    for k, v in ROOTS.items():
        if ref.startswith(k + "/"):
            return os.path.normpath(os.path.join(v, ref[len(k) + 1:]))
    return ref if os.path.isabs(ref) else os.path.normpath(os.path.join(cfg_dir, ref))


def validate(cfg, cfg_dir):
    errs = []
    slides = cfg.get("slides") or []
    if not slides:
        errs.append("no slides")
    tr = float(cfg.get("transition", {}).get("duration", 0.4))
    total = sum(float(s.get("duration", 2.5)) for s in slides) - tr * max(0, len(slides) - 1)
    if not (MIN_LEN <= total <= MAX_LEN):
        errs.append(f"total length {total:.2f}s outside {MIN_LEN}-{MAX_LEN}s")
    banned = [r"free shipping", r"only \d+ left", r"selling out", r"last chance", r"\bQR\b",
              r"coupon", r"promo code", r"\bcode\b", r"5[- ]star", r"best[- ]seller", r"#1\b"]
    alltext = " ".join(t.get("text", "") for s in slides for t in s.get("texts", []))
    alltext += " " + cfg.get("caption", "") + " " + cfg.get("footer", "")
    for b in banned:
        if re.search(b, alltext, re.I):
            errs.append(f"banned phrase matched: /{b}/")
    if re.search(r"\$\s?\d", alltext) and not cfg.get("prices_verified_on"):
        errs.append("price on screen/caption without prices_verified_on date (must match live store)")
    for i, s in enumerate(slides):
        for ref in s.get("images", [s.get("image")]):
            if not ref:
                errs.append(f"slide {i+1}: no image"); continue
            p = resolve_image(ref, cfg_dir) if not re.match(r"https?://", ref) else None
            if p and not os.path.exists(p):
                errs.append(f"slide {i+1}: image not found: {p}")
        for t in s.get("texts", []):
            if t.get("style", "body") not in STYLES:
                errs.append(f"slide {i+1}: unknown style {t.get('style')}")
    return errs, total


def fit_image(img, box_w, box_h, mode):
    iw, ih = img.size
    s = (max if mode == "cover" else min)(box_w / iw, box_h / ih)
    return img.resize((max(1, round(iw * s)), max(1, round(ih * s))), Image.LANCZOS)


def build_base(slide, cfg_dir, scale):
    """Background + product image at W*scale x H*scale (extra room for motion)."""
    BW, BH = round(W * scale), round(H * scale)
    if "images" in slide:  # 2-4 image grid (picks / matching sets)
        return build_grid(slide, cfg_dir, scale)
    img = Image.open(resolve_image(slide["image"], cfg_dir)).convert("RGB")
    bg = slide.get("bg", "blur")
    if bg == "blur":
        base = fit_image(img, BW, BH, "cover")
        l, t = (base.width - BW) // 2, (base.height - BH) // 2
        base = base.crop((l, t, l + BW, t + BH)).filter(ImageFilter.GaussianBlur(40 * scale))
        base = Image.blend(base, Image.new("RGB", base.size, col("cream")[:3]), 0.35)
    else:
        base = Image.new("RGB", (BW, BH), col(bg)[:3])
    fit = slide.get("fit", "contain")
    if fit == "cover":
        fx, fy = slide.get("focus", [0.5, 0.5])
        im = fit_image(img, BW, BH, "cover")
        l = round((im.width - BW) * fx); t = round((im.height - BH) * fy)
        base.paste(im.crop((l, t, l + BW, t + BH)), (0, 0))
    else:
        # contain inside an image box (default: centre band of the safe zone)
        bx = slide.get("box", [40, 400, 1040, 1400])  # x0,y0,x1,y1 in output px
        bx = [round(v * scale) for v in bx]
        # account for zoom growth around centre: box is in final-frame coords
        off_x, off_y = (BW - W * scale) / 2, (BH - H * scale) / 2
        im = fit_image(img, bx[2] - bx[0], bx[3] - bx[1], "contain")
        x = round(bx[0] + off_x + (bx[2] - bx[0] - im.width) / 2)
        y = round(bx[1] + off_y + (bx[3] - bx[1] - im.height) / 2)
        if slide.get("shadow", True):
            sh = Image.new("RGBA", base.size, (0, 0, 0, 0))
            ImageDraw.Draw(sh).rounded_rectangle([x + 10, y + 18, x + im.width + 10, y + im.height + 18],
                                                 radius=int(24 * scale), fill=(0, 0, 0, 90))
            sh = sh.filter(ImageFilter.GaussianBlur(18 * scale))
            base = Image.alpha_composite(base.convert("RGBA"), sh).convert("RGB")
        mask = Image.new("L", im.size, 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, im.width - 1, im.height - 1],
                                               radius=int(slide.get("radius", 28) * scale), fill=255)
        base.paste(im, (x, y), mask)
    return base


def build_grid(slide, cfg_dir, scale):
    BW, BH = round(W * scale), round(H * scale)
    bg = slide.get("bg", "cream")
    base = Image.new("RGB", (BW, BH), col(bg if bg != "blur" else "cream")[:3])
    ims = [Image.open(resolve_image(r, cfg_dir)).convert("RGB") for r in slide["images"]]
    bx = [round(v * scale) for v in slide.get("box", [60, 500, 1020, 1340])]
    gap = round(20 * scale)
    n = len(ims)
    if n == 2 and slide.get("layout", "row") == "row":
        cells = [(bx[0], bx[1], (bx[0] + bx[2] - gap) // 2, bx[3]), ((bx[0] + bx[2] + gap) // 2, bx[1], bx[2], bx[3])]
    elif n == 2:
        cells = [(bx[0], bx[1], bx[2], (bx[1] + bx[3] - gap) // 2), (bx[0], (bx[1] + bx[3] + gap) // 2, bx[2], bx[3])]
    else:
        mx, my = (bx[0] + bx[2]) // 2, (bx[1] + bx[3]) // 2
        cells = [(bx[0], bx[1], mx - gap // 2, my - gap // 2), (mx + gap // 2, bx[1], bx[2], my - gap // 2),
                 (bx[0], my + gap // 2, mx - gap // 2, bx[3]), (mx + gap // 2, my + gap // 2, bx[2], bx[3])]
    labels = slide.get("labels", [])
    d = ImageDraw.Draw(base)
    for k, (im, c) in enumerate(zip(ims, cells)):
        cw, ch = c[2] - c[0], c[3] - c[1]
        f = fit_image(im, cw, ch, "cover")
        l, t = (f.width - cw) // 2, (f.height - ch) // 2
        f = f.crop((l, t, l + cw, t + ch))
        mask = Image.new("L", f.size, 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, cw - 1, ch - 1], radius=round(24 * scale), fill=255)
        base.paste(f, (c[0], c[1]), mask)
        if k < len(labels):
            fnt = font("black", round(54 * scale)); r = round(40 * scale)
            cx, cy = c[0] + r + round(14 * scale), c[1] + r + round(14 * scale)
            d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col("berry")[:3])
            tw = d.textlength(labels[k], font=fnt)
            asc, desc = fnt.getmetrics()
            d.text((cx - tw / 2, cy - (asc + desc) / 2 - round(2 * scale)), labels[k], font=fnt, fill=col("cream")[:3])
    return base


def wrap(draw, text, fnt, max_w):
    lines = []
    for para in text.split("\n"):
        words, cur = para.split(), ""
        for w_ in words:
            trial = (cur + " " + w_).strip()
            if draw.textlength(trial, font=fnt) <= max_w or not cur:
                cur = trial
            else:
                lines.append(cur); cur = w_
        lines.append(cur)
    return lines


def text_block(t):
    """Render one text card to RGBA; returns image."""
    st = dict(STYLES[t.get("style", "body")])
    st.update({k: t[k] for k in ("size", "color", "card") if k in t})
    fnt = font(st["font"], st["size"])
    tmp = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    pad = st["pad"]
    max_w = (SAFE["right"] - SAFE["left"]) - 2 * pad
    lines = wrap(tmp, t["text"], fnt, max_w)
    if len(lines) > 1 and "\n" not in t["text"]:  # balance line lengths (no lonely last word)
        n, w_try = len(lines), max_w
        while w_try > 200:
            trial = wrap(tmp, t["text"], fnt, w_try - 10)
            if len(trial) > n:
                break
            lines, w_try = trial, w_try - 10
    asc, desc = fnt.getmetrics()
    lh = round((asc + desc) * 1.02)
    tw = max(tmp.textlength(l, font=fnt) for l in lines)
    bw, bh = int(tw + 2 * pad), int(lh * len(lines) + 2 * pad - (desc * 0.35))
    m = 16  # margin for the soft shadow
    im = Image.new("RGBA", (bw + 2 * m, bh + 2 * m), (0, 0, 0, 0))
    if st["card"]:
        sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle([m, m + 5, m + bw - 1, m + bh + 4], radius=min(28, bh // 3), fill=(0, 0, 0, 70))
        im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(7)))
    d = ImageDraw.Draw(im)
    if st["card"]:
        d.rounded_rectangle([m, m, m + bw - 1, m + bh - 1], radius=min(28, bh // 3), fill=col(st["card"], st["alpha"]))
    for i, l in enumerate(lines):
        lw = d.textlength(l, font=fnt)
        d.text((m + (bw - lw) / 2, m + pad + i * lh - desc * 0.15), l, font=fnt, fill=col(st["color"]))
    return im


def build_overlay(slide, footer):
    """Static text layer for a slide, laid out inside SAFE."""
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cx = (SAFE["left"] + SAFE["right"]) // 2
    groups = {"top": [], "middle": [], "bottom": []}
    for t in slide.get("texts", []):
        groups[t.get("position", "top")].append(text_block(t))
    gap = 18 - 2 * 16  # cards carry a 16px shadow margin each side
    footer_h = 0
    if footer:
        fb = text_block({"text": footer, "style": "small"})
        footer_h = fb.height + gap
        ov.alpha_composite(fb, (cx - fb.width // 2, SAFE["bottom"] - fb.height + 16))
    y = SAFE["top"] - 16
    for b in groups["top"]:
        ov.alpha_composite(b, (cx - b.width // 2, y)); y += b.height + gap
    y = SAFE["bottom"] - footer_h + (16 if not footer else 0)
    for b in reversed(groups["bottom"]):
        y -= b.height; ov.alpha_composite(b, (cx - b.width // 2, y)); y -= gap
    mh = sum(b.height for b in groups["middle"]) + gap * max(0, len(groups["middle"]) - 1)
    y = (SAFE["top"] + SAFE["bottom"]) // 2 - mh // 2
    for b in groups["middle"]:
        ov.alpha_composite(b, (cx - b.width // 2, y)); y += b.height + gap
    return ov


def motion_frame(base, motion, p, scale):
    """Crop a W x H window out of the oversized base for progress p in [0,1]."""
    BW, BH = base.size
    ease = p * p * (3 - 2 * p)
    zmax = scale  # base is `scale` x the frame
    if motion == "zoom_in":
        z = 1.0 + (zmax - 1.0) * 0.85 * ease
    elif motion == "zoom_out":
        z = 1.0 + (zmax - 1.0) * 0.85 * (1 - ease)
    else:
        z = 1.0 + (zmax - 1.0) * 0.5
    vw, vh = BW / z, BH / z  # visible window in base px
    cx, cy = BW / 2, BH / 2
    if motion == "pan_left":
        cx = BW / 2 + (BW - vw) / 2 * (1 - 2 * ease) * 0.9
    elif motion == "pan_up":
        cy = BH / 2 + (BH - vh) / 2 * (1 - 2 * ease) * 0.9
    box = (cx - vw / 2, cy - vh / 2, cx + vw / 2, cy + vh / 2)
    return base.transform((W, H), Image.EXTENT, box, Image.BICUBIC)


def render(cfg_path, qa=False, out_override=None):
    cfg = load_config(cfg_path)
    cfg_dir = os.path.dirname(os.path.abspath(cfg_path))
    errs, total = validate(cfg, cfg_dir)
    if errs:
        raise SystemExit(f"[{cfg_path}] config errors:\n  - " + "\n  - ".join(errs))
    fps = int(cfg.get("fps", 30))
    tr = float(cfg.get("transition", {}).get("duration", 0.4))
    scale = float(cfg.get("motion_scale", 1.08))
    footer = cfg.get("footer", "")
    vid = cfg["id"]
    out = out_override or os.path.join(cfg_dir, cfg.get("output", f"../out/{vid}.mp4"))
    out = os.path.normpath(out); os.makedirs(os.path.dirname(out), exist_ok=True)

    slides = cfg["slides"]
    bases = [build_base(s, cfg_dir, scale) for s in slides]
    overlays = [build_overlay(s, footer) for s in slides]
    durs = [float(s.get("duration", 2.5)) for s in slides]
    starts, t = [], 0.0
    for d in durs:
        starts.append(t); t += d - tr
    nframes = round(total * fps)

    def slide_frame(i, tt):
        local = tt - starts[i]
        fr = motion_frame(bases[i], slides[i].get("motion", "zoom_in"), min(1, max(0, local / durs[i])), scale)
        fr = fr.convert("RGBA")
        a = min(1.0, max(0.0, (local - (0.15 if i else 0)) / 0.3)) if slides[i].get("text_fade", True) else 1
        ov = overlays[i]
        if a < 1:
            ov = ov.copy(); ov.putalpha(ov.getchannel("A").point(lambda v: int(v * a)))
        fr.alpha_composite(ov)
        return fr.convert("RGB")

    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
           "-s", f"{W}x{H}", "-r", str(fps), "-i", "-", "-an", "-c:v", "libx264",
           "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-profile:v", "high",
           "-movflags", "+faststart", "-r", str(fps), out]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    qa_frames = {}
    mids = [starts[i] + durs[i] / 2 for i in range(len(slides))]
    for n in range(nframes):
        tt = n / fps
        cur = max(i for i in range(len(slides)) if starts[i] <= tt + 1e-9)
        fr = slide_frame(cur, tt)
        # crossfade: if next slide has started (overlap window), blend
        if cur > 0 and tt < starts[cur] + tr:
            prev = slide_frame(cur - 1, tt)
            fr = Image.blend(prev, fr, (tt - starts[cur]) / tr)
        proc.stdin.write(fr.tobytes())
        if qa:
            for i, m in enumerate(mids):
                if abs(tt - m) < 0.5 / fps:
                    qa_frames[i] = fr.copy()
    proc.stdin.close()
    if proc.wait() != 0:
        raise SystemExit(f"ffmpeg failed for {cfg_path}")

    if qa:
        qdir = os.path.join(os.path.dirname(out), "qa")
        os.makedirs(qdir, exist_ok=True)
        for i, fr in sorted(qa_frames.items()):
            fr.save(os.path.join(qdir, f"{vid}-s{i+1:02d}.jpg"), quality=88)
        if 0 in qa_frames:
            sz = qa_frames[0].convert("RGBA")
            shade = Image.new("RGBA", (W, H), (255, 0, 0, 70))
            d = ImageDraw.Draw(shade)
            d.rectangle([SAFE["left"], SAFE["top"], SAFE["right"], SAFE["bottom"]], fill=(0, 0, 0, 0),
                        outline=(255, 0, 0, 255), width=4)
            sz.alpha_composite(shade)
            sz.convert("RGB").save(os.path.join(qdir, f"{vid}-safezone.jpg"), quality=85)
    probe = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                            "format=duration:stream=codec_type,width,height", "-of", "json", out],
                           capture_output=True, text=True)
    info = json.loads(probe.stdout)
    streams = [s["codec_type"] for s in info["streams"]]
    print(f"{vid}: {out}  {float(info['format']['duration']):.2f}s  streams={streams}")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("configs", nargs="+")
    ap.add_argument("--qa", action="store_true", help="write per-slide QA frames + safe-zone preview")
    ap.add_argument("--check", action="store_true", help="validate only")
    a = ap.parse_args()
    bad = 0
    for c in a.configs:
        if a.check:
            errs, total = validate(load_config(c), os.path.dirname(os.path.abspath(c)))
            print(f"{c}: {total:.2f}s", "OK" if not errs else errs); bad += bool(errs)
        else:
            render(c, qa=a.qa)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
