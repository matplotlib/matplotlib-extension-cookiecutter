#!/usr/bin/env python
import os
import subprocess
from contextlib import suppress

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":
    if "No license" == "{{ cookiecutter.license }}":
        remove_file("LICENSE")

    with suppress(Exception):
        subprocess.run(["git", "init", "-q"])
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-q", "-m", "initial commit"])
