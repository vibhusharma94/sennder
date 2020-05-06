#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

NAME = 'sennder'
DESCRIPTION = 'Rest Api using flask'
URL = 'https://github.com//vibhusharma94/sennder'
EMAIL = 'vibhu.evs@gmail.com'
AUTHOR = 'Vibhu Sharma'


def get_requirements(env):
    with open('requirements.txt'.format(env)) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


install_requires = get_requirements('base')

setup(
    name=NAME,
    version=0.1,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages('sennder'),
    package_dir={'': 'sennder'},
    install_requires=install_requires,

)
