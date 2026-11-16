#!/usr/bin/env bash
# Render every config in configs/ (or the ones passed) in parallel, with QA frames.
set -euo pipefail
cd "$(dirname "$0")"
if [ $# -gt 0 ]; then CFGS=("$@"); else CFGS=(configs/*.json); fi
python3 render.py --check "${CFGS[@]}"
printf '%s\n' "${CFGS[@]}" | xargs -P "${JOBS:-4}" -n 1 python3 render.py --qa
