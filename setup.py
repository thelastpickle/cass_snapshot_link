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
