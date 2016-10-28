import subprocess
from setuptools import setup, find_packages, Extension

from setuptools.command.install import install as _install

# Because of relative paths, this must be run from inside numbuf/.

class install(_install):
  def run(self):
    subprocess.check_call(["./setup.sh"])
    subprocess.check_call(["./build.sh"])
    _install.run(self)

setup(name="numbuf",
      version="0.0.1",
      packages=find_packages(),
      package_data={"numbuf": ["libnumbuf.so"]},
      cmdclass={"install": install},
      zip_safe=False)
