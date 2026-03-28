#!/usr/bin/env python
from setuptools import setup
import greenwithenvy


setup(
    name='greenwithenvy',
    version=greenwithenvy.VERSION,
    description='Easy GPU switching for Nvidia Optimus laptops under Linux',
    url='http://github.com/bayasdev/greenwithenvy',
    author='Victor Bayas',
    author_email='victorsbayas@gmail.com',
    license='MIT',
    py_modules=['greenwithenvy'],
    entry_points={
        'console_scripts': [
            'greenwithenvy=greenwithenvy:main',
        ],
    },
    keywords=['nvidia', 'optimus', 'prime', 'gpu', 'linux'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux'
    ],
)