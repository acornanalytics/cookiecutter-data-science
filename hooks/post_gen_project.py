"""Remove the empty LICENSE when no license is chosen, then initialize git and sync."""

import os
import subprocess

if "{{ cookiecutter.open_source_license }}" == "No license file":
    os.remove("LICENSE")

subprocess.run(["git", "init", "-q", "-b", "main"], check=False)
if subprocess.run(["uv", "sync", "-q"], check=False).returncode != 0:
    print("uv sync failed or uv is not installed; run `uv sync` manually.")
