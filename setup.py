#!/usr/bin/env python
from setuptools import setup
import greenwithenvy


setup(
    name='greenwithenvy',
    version=greenwithenvy.VERSION,
    description='Easy GPU switching for Nvidia Optimus laptops under Linux',
    url='http://github.com/lechibang-1512/greenwithenvy',
    author='lechibang-1512',
    author_email='throwawaybard76@gmail.com',
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