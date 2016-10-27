import subprocess
from setuptools import setup, find_packages, Extension

from setuptools.command.build_ext import build_ext as _build_ext

# Because of relative paths, this must be run from inside numbuf/.

class build_ext(_build_ext):
  def run(self):
    subprocess.check_call(["./setup.sh"])
    subprocess.check_call(["./build.sh"])
    _build_ext.run(self)

setup(name="numbuf",
      version="0.0.1",
      packages=find_packages(),
      package_data={"numbuf": ["libnumbuf.so"]},
      cmdclass={"build_ext": build_ext},
      zip_safe=False)
