#!/usr/bin/env python
# encoding: utf-8

# Copyright 2012 Aaron Morton
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from setuptools import setup

entry_points = """
[console_scripts]
cass_snapshot_link = cass_snapshot_link:main
"""

#doubt this is the right way to do this
import sys
major, minor, _, _, _ = sys.version_info
if (major == 2 and minor < 7) or (major == 2 and minor < 2):
    install_requires = ["argparse>1.2"]
else:
    install_requires = []

setup(
    name='cass_snapshot_link',
    version='0.1.0',
    author='Aaron Morton',
    author_email='aaron@thelastpickle.com',
    packages = [],
    install_requires=install_requires,
    entry_points=entry_points
)
