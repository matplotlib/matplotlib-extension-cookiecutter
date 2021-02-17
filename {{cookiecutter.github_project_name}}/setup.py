from os import path

from setuptools import find_packages, setup

# extract version
path = path.realpath("{{ cookiecutter.python_package_name }}/_version.py")
version_ns = {}
with open(path, encoding="utf8") as f:
    exec(f.read(), {}, version_ns)
version = version_ns["__version__"]

setup_args = dict(
    version=version,
)

if __name__ == "__main__":
    setup(**setup_args)
