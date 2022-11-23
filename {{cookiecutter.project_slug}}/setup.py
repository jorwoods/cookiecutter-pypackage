#!/usr/bin/env python

"""The setup script."""

from setuptools import setup
{%- if cookiecutter.use_versioneer %}
import versioneer
{%- endif %}

setup(
{%- if cookiecutter.use_versioneer %}
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
{%- endif %}
)
