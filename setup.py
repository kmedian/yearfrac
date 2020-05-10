from setuptools import setup


def read(fname):
    import os
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='yearfrac',
      version='0.4.3',
      description='Daycount methods to compute date differences in year units',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='http://github.com/kmedian/yearfrac',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['yearfrac'],
      install_requires=[
          'setuptools>=40.0.0',
          'numpy>=1.14.*',
          'six>=1.13.*'],
      python_requires='>=3.6',
      zip_safe=False)
