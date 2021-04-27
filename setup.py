from setuptools import setup
import os


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as fp:
        s = fp.read()
    return s


def get_version(path):
    with open(path, "r") as fp:
        lines = fp.read()
    for line in lines.split("\n"):
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(name='yearfrac',
      version=get_version("yearfrac/__init__.py"),
      description='Daycount methods to compute date differences in year units',
      long_description=read('README.rst'),
      url='http://github.com/kmedian/yearfrac',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['yearfrac'],
      install_requires=[
          'numpy>=1.14.*,<2'],
      python_requires='>=3.6',
      zip_safe=True)
