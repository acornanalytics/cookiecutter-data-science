#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
core.py

Created on `{% now 'local', '%Y-%m-%d' %}
by {{ cookiecutter.author_name }}
{{ cookiecutter.author_email }}
"""
import logging as log

def main():
    # TODO:
    # run its processes
    pass

if __name__ == "__main__":
    log.basicConfig(level=log.DEBUG,
                    format='%(asctime)s %(message)s',
                    datefmt="%b %d %H:%M:%S %Z")

    main()
