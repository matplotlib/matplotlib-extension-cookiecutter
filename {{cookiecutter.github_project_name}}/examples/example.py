"""
------------
Example Name
------------

A short example showcasing how to use the library. The docstrings will be
converted to RST by sphinx-gallery.
"""

import numpy as np
import matplotlib.pyplot as plt
from {{ cookiecutter.python_package_name }} import example_function


# make some fake data
rng = np.random.default_rng(0)
data = rng.standard_normal((1000, 2))

fig, ax = plt.subplots()
scatter = example_function(ax, data, above_color='b')
plt.show()
