#!/usr/bin/env python
# coding: utf-8

# Copyright (c) {{ cookiecutter.author_name }}.
# Distributed under the terms of the Modified BSD License.

__all__ = [
    "example_function",
]
import numpy as np


def example_function(ax, data, above_color="r", below_color="k", **kwargs):
    """
    An example function that makes a scatter plot with points colored differently
    depending on if they are above or below `y=0`.

    Parameters
    ----------
    ax : matplotlib axis
        The axis to plot on.
    data : (N, 2) array-like
        The data to make a plot from
    above_color : color-like, default: 'r'
        The color of points with `y>0`
    below_color : color-like, default: 'k'
        The color of points with `y<0`
    kwargs :
        Passed through to `ax.scatter`

    Returns
    -------
    MarkerCollection
    """
    colors = np.array([above_color] * data.shape[0])
    colors[data[:, 1] < 0] = below_color
    return ax.scatter(data[:, 0], data[:, 1], c=colors, **kwargs)
