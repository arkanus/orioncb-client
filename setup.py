# -*- coding: utf-8 -*-
import sys
from setuptools import setup

setup(
    name='orion-client',
    version='0.0.1',
    author='Marcos Sánchez',
    author_email='arkanus@gmail.com',
    description="Fiware's Orion Context Broker client lib",
    py_modules=['orion'],
    # url='https://github.com/arkanus/selenium-sunbro',
    license='Mozilla Public License 2.0 (MPL 2.0)',
    keywords='fiware orion context broker IoT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ],
    install_requires=['requests>=2.5.0'],
    test_suite="tests",
)
