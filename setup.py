# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ds-project-template',
    version='1.0.0',
    description='Sample template for data science project',
    long_description=readme,
    author='Ujwal Reddy',
    author_email='hidden@gmail.com',
    url='https://github.com/ujwal-projects/ds-project-template',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)