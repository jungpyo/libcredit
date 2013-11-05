#! /usr/bin/env python

from distutils.core import setup
from DistUtilsExtra.command import (build_extra, build_i18n)

setup(
    name='libcredit.py',
    version='0.1.0',
    packages=['libcredit'],
    package_dir = { '': 'python' },
    cmdclass={
        "build": build_extra.build_extra,
        "build_i18n": build_i18n.build_i18n,
    },
)
