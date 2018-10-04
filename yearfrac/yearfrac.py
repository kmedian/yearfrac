import collections
from .method_factory import methods


def __yearfrac_scalar_scalar(s1, s2, method_function):
    return method_function(
        s1.year, s1.month, s1.day,
        s2.year, s2.month, s2.day
    )


def __yearfrac_scalar_vector(s, v, method_function):
    sv = [s] * len(v)
    __yearfrac_vector_vector(sv, v, method_function)


def __yearfrac_vector_scalar(v, s, method_function):
    sv = [s] * len(v)
    __yearfrac_vector_vector(v, sv, method_function)


def __yearfrac_vector_vector(v1, v2, method_function):
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


def yearfrac(d1, d2, method='act'):
    yearfrac_func = __algorithm_mapper[
        (
            isinstance(d1, collections.Iterable),
            isinstance(d2, collections.Iterable)
        )
    ]
    method_function = methods[method]
    return yearfrac_func(d1, d2, method_function)
