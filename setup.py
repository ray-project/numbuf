import subprocess
from setuptools import setup, find_packages, Extension

# Because of relative paths, this must be run from inside numbuf/.

subprocess.check_call(["./setup.sh"])
subprocess.check_call(["./build.sh"])

setup(name="numbuf",
      version="0.0.1",
      packages=find_packages(),
      package_data={"numbuf": ["libnumbuf.so"]},
      include_package_data=True,
      zip_safe=False)
