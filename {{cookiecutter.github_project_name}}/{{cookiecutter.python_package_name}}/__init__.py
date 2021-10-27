#!/usr/bin/env python
# coding: utf-8

# Copyright (c) {{ cookiecutter.author_name }}.
# Distributed under the terms of the Modified BSD License.

# Must import __version__ first to avoid errors importing this file during the build process.
# See https://github.com/pypa/setuptools/issues/1724#issuecomment-627241822
try:
    from ._version import __version__
except ImportError:
    __version__ = "unknown"

from .example import example_function


__all__ = [
    "__version__",
    "example_function",
]
