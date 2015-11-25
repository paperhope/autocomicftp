#!/usr/bin/env python

from setuptools import setup

setup(name='Autocomicftp',
      version='0.1',
      description='Autocomic web app',
      author='Håvard Futsæter',
      author_email='futsaeter@gmail.com',
      packages=['autocomicftp'],
      install_requires = [
          "flask",
          ]
          
     )
