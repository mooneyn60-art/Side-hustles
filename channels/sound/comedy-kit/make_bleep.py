#!/usr/bin/env python3
"""Make a 1 kHz sine bleep of any length (in-house, 2026-11-16).

Usage:
    python3 make_bleep.py DURATION_SECONDS [OUT.wav]

Examples:
    python3 make_bleep.py 0.3
    python3 make_bleep.py 0.8 /tmp/bleep-0.8s.wav

Defaults: 1000 Hz sine, 5 ms fade in and out, 48 kHz 16-bit mono WAV,
peak -3 dBFS. Duration is the full file length including the fades.
"""
from __future__ import annotations

import sys
import wave
from pathlib import Path

import numpy as np

SR = 48000
FREQ = 1000.0
FADE_S = 0.005
PEAK_DB = -3.0


def bleep(duration, sr=SR, freq=FREQ, fade_s=FADE_S, peak_db=PEAK_DB):
    if duration <= 0:
        raise SystemExit("duration must be positive")
    n = int(round(duration * sr))
    t = np.arange(n, dtype=np.float64) / sr
    x = np.sin(2 * np.pi * freq * t)
    fade_n = min(int(round(fade_s * sr)), n // 2)
    env = np.ones(n, dtype=np.float64)
    if fade_n > 0:
        env[:fade_n] = np.linspace(0, 1, fade_n, endpoint=True)
        env[-fade_n:] = np.linspace(1, 0, fade_n, endpoint=True)
    x *= env
    peak = 10 ** (peak_db / 20)
    x *= peak / (np.max(np.abs(x)) + 1e-12)
    return x.astype(np.float32)


def write_wav(path, audio, sr=SR):
    path = Path(path)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes((np.clip(audio, -1, 1) * 32767).astype("<i2").tobytes())


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] in {"-h", "--help"}:
        print(__doc__.strip())
        return 0
    duration = float(argv[0])
    out = Path(argv[1]) if len(argv) > 1 else Path(f"bleep-{duration:g}s.wav")
    write_wav(out, bleep(duration))
    print(f"wrote {out}  {duration:g}s  1 kHz  peak {PEAK_DB} dBFS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
