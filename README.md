[![Build Status](https://travis-ci.org/kmedian/yearfrac.svg?branch=master)](https://travis-ci.org/kmedian/yearfrac)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/kmedian/yearfrac/master?urlpath=lab)

# yearfrac


## Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [Commands](#commands)
* [Support](#support)
* [Contributing](#contributing)


## Installation
The `yearfrac` [git repo](http://github.com/kmedian/yearfrac) is available as [PyPi package](https://pypi.org/project/yearfrac)

```
pip install yearfrac
```


## Usage
Check the [examples](examples) folder for notebooks.

Functions

* `isaleapyear` -- Check if a year is leap year
* `eastersunday` -- Determine day and month of an Easter Sunday for a given year
* `jd_to_date` and `date_to_jd` -- Julian Day number conversion
* `act_afb` -- Actual/Actual AFB
* `act_isda` -- Actual/Actual ISDA
* `yearfrac` -- Wrapper for all daycount methods

## Commands
* Check syntax: `flake8 --ignore=F401`
* Run Unit Tests: `python -W ignore -m unittest discover`
* Remove `.pyc` files: `find . -type f -name "*.pyc" | xargs rm`
* Remove `__pycache__` folders: `find . -type d -name "__pycache__" | xargs rm -rf`
* Upload to PyPi with twine: `python setup.py sdist && twine upload -r pypi dist/*`


## Debugging
* Notebooks to profile python code are in the [profile](profile) folder


## Support
Please [open an issue](https://github.com/kmedian/yearfrac/issues/new) for support.


## Contributing
Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/kmedian/yearfrac/compare/).
