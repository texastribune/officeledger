#!/usr/bin/env python
from distutils.core import setup

# Dynamically calculate the version based on mptt.VERSION
version_tuple = (0, 2, 0, 'alpha', 0)
version = ".".join([str(v) for v in version_tuple])

setup(
    name = 'officeledger',
    description = '''A tool for keeping track of what people owe.''',
    version = version,
    author = 'Texas Tribune',
    url = 'http://github.com/texastribune/officeledger',
    packages=['officeledger'],
    package_dir={'officeledger': 'officeledger'},
    package_data={'officeledger': ['templates/*']},
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)

