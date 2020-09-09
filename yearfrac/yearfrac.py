from collections.abc import Iterable
from .method_factory import methods
import datetime
import numpy as np


def __yearfrac_scalar_scalar(s1: datetime.datetime,
                             s2: datetime.datetime,
                             method_function) -> float:
    return method_function(
        s1.year, s1.month, s1.day,
        s2.year, s2.month, s2.day
    )


def __yearfrac_scalar_vector(s: datetime.datetime,
                             v: np.ndarray,
                             method_function) -> list:
    sv = [s] * len(v)
    __yearfrac_vector_vector(sv, v, method_function)


def __yearfrac_vector_scalar(v: np.ndarray,
                             s: datetime.datetime,
                             method_function) -> list:
    sv = [s] * len(v)
    __yearfrac_vector_vector(v, sv, method_function)


def __yearfrac_vector_vector(v1: np.ndarray,
                             v2: np.ndarray,
                             method_function) -> list:
    rows = zip(v1, v2)
    return [
        method_function(
            s1.year, s1.month, s1.day,
            s2.year, s2.month, s2.day
        )
        for s1, s2 in rows
    ]


__algorithm_mapper = {
    (True, True): __yearfrac_vector_vector,
    (False, False): __yearfrac_scalar_scalar,
    (True, False):
        lambda v, s, m: __yearfrac_vector_vector(v, [s] * len(v), m),
    (False, True):
        lambda s, v, m: __yearfrac_vector_vector([s] * len(v), v, m)
}


# output is list or float
def yearfrac(d1: datetime.datetime,
             d2: datetime.datetime,
             method: str = 'act'):
    yearfrac_func = __algorithm_mapper[
        (
            isinstance(d1, Iterable),
            isinstance(d2, Iterable)
        )
    ]
    method_function = methods[method]
    return yearfrac_func(d1, d2, method_function)
