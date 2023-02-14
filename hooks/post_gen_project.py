#!/usr/bin/env python
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd().resolve().absolute()


def remove_file(filepath):
    (PROJECT_DIRECTORY / filepath).unlink()


if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = Path("src", '{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if "{{ cookiecutter.package_manager }}" != "pip":
        remove_file("requirements_dev.txt")
