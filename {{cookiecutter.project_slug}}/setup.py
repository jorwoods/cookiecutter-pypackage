#!/usr/bin/env python

"""The setup script."""

from setuptools import setup
{%- if cookiecutter.version_manager == "versioneer" %}
import versioneer
{%- endif %}

setup(
{%- if cookiecutter.version_manager == "versioneer" %}
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
{%- endif %}
)
