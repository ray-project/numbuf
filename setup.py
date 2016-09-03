import sys

from setuptools import setup, find_packages

# Because of relative paths, this must be run from inside numbuf/.

setup(
  name = "numbuf",
  version = "0.1.dev0",
  use_2to3=True,
  packages=find_packages(),
  package_data = {
    "numbuf": ["libnumbuf.so"]
  },
  zip_safe=False,
)
