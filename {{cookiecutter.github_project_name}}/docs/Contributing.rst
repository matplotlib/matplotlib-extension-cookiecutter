============
Contributing
============

Thanks for thinking of a way to help improve this library! Remember that contributions come in all
shapes and sizes beyond writing bug fixes. Contributing to documentation, opening new `issues <https://github.com/{{ cookiecutter.github_organization_name }}/{{ cookiecutter.github_project_name }}/issues>`_,
asking for clarification on things you find unclear, and requesting new features, are all super valuable contributions. 

Code Improvements
-----------------

All development for this library happens at https://github.com/{{ cookiecutter.github_organization_name }}/{{ cookiecutter.github_project_name }},

First set up a dev environment. The instructions here use `mamba <https://github.com/mamba-org/mamba#mamba>`_ which is open source
implementation of `conda` that offers significant speed ups. You can substitute ``conda`` for ``mamba`` or use ``venv`` without any ill-effects.

.. code-block:: bash

    mamba create -n {{ cookiecutter.python_package_name}}-dev python
    conda activate {{ cookiecutter.python_package_name}}-dev

Now clone your fork of the Git repository and make an editable (``-e``) install.

.. code-block:: bash
   
   git clone <your fork>
   cd {{ cookiecutter.github_project_name }}
   pip install -e ".[dev]"


Working with Git
^^^^^^^^^^^^^^^^

Using Git/Github can confusing (https://xkcd.com/1597/) so if you're new to Git, you may find
it helpful to use a program like `Github Desktop <desktop.github.com>`_ and to follow
a `guide <https://github.com/firstcontributions/first-contributions#first-contributions>`_. 

Also feel free to ask for help/advice on the relevant Github `issue <https://github.com/{{ cookiecutter.github_organization_name }}/{{ cookiecutter.github_project_name }}/issues>`_.

Documentation
-------------

Following changes to the source files, you can view recent adjustments by building the documentation.

1. Make sure you have installed the requirements for building the documentation:

.. code-block:: bash

    cd {{ cookiecutter.github_project_name }}
    pip install -e ".[doc]"

2. Run the following commands:

.. code-block:: bash

    cd docs
    make html

If you open the ``_build/html/index.html`` file in your browser you should now be able to see the rendered documentation.

Autobuild the documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Alternatively, you can use `sphinx-autobuild <https://github.com/GaretJax/sphinx-autobuild>`_ to continuously watch the documentation for changes and rebuild it for you.
Sphinx-autobuild will be installed automatically by the above ``pip`` command, and we've added it to the ``Makefile``. All you need to do is:

.. code-block:: bash

    cd docs
    make watch

In a few seconds your web browser should open up the documentation. Now whenever you save a file
the documentation will automatically regenerate and the webpage will refresh for you!
