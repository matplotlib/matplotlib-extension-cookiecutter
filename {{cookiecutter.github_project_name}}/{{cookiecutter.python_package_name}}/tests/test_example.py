#!/usr/bin/env python
# coding: utf-8

# Copyright (c) {{ cookiecutter.author_name }}.
# Distributed under the terms of the Modified BSD License.

from ..example import example_function


import pytest
import matplotlib.pyplot as plt
import numpy as np


@pytest.mark.mpl_image_compare(filename="test_example.png")
def test_example():
    fig, ax = plt.subplots()
    # data = np.hstack([np.linspace(-10, 10)[:, None], np.linspace(10, -10)[:, None]])
    example_function(ax, data, above_color='b', below_color='g')
    return fig
