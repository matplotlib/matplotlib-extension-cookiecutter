from setuptools import setup

{% if cookiecutter.version_control == 'setuptools-scm' -%}
setup_args = dict(
    use_scm_version={"write_to": "{{cookiecutter.python_package_name}}/_version.py"}
)
{%- else -%}
setup_args = dict()
{%- endif %}

if __name__ == "__main__":
    setup(**setup_args)
