#!/usr/bin/env python3
"""Coolest art entry: writes the bundled weeping eye with planet Earth as its iris (chalk mural style) to /output/entry.png.
The image is shipped in the repository; this program copies it, byte-identical on every run (no network)."""
import os, shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUT_DIR, "entry.png"))
