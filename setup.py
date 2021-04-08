from setuptools import setup
import pypandoc


setup(name='yearfrac',
      version='0.4.4',
      description='Daycount methods to compute date differences in year units',
      long_description=pypandoc.convert('README.md', 'rst'),
      url='http://github.com/kmedian/yearfrac',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['yearfrac'],
      install_requires=[
          'setuptools>=40.0.0',
          'numpy>=1.14.*'],
      python_requires='>=3.6',
      zip_safe=True)
