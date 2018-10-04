import collections
from .act_isda import act_isda
from .act_afb import act_afb
from .d30360e import d30360e


def __get_method_function(method):
    if method.lower() in ('act', 'act_afb', 'afb'):
        return act_afb
    elif method.lower() == 'act_isda':
        return act_isda
    elif method.lower() in ('d30360e', '30e360'):
        return lambda x1,x2,x3,y1,y2,y3: d30360e(
            x1, x2, x3,
            y1, y2, y3,
            False
        )
    elif method.lower() in ('d30360e_matu', '30e360_matu'):
        return lambda x1, x2, x3, y1, y2, y3: d30360e(
            x1, x2, x3,
            y1, y2, y3,
            True
        )
    raise Exception("no method {0:s}".format(method))


def __yearfrac_scalar_scalar(s1, s2, method_function):
    return method_function(
        s1.year, s1.month, s1.day,
        s2.year, s2.month, s2.day
    )


def __yearfrac_scalar_vector(s, v, method_function):
    sv = [s]*len(v)
    __yearfrac_vector_vector(sv, v, method_function)


def __yearfrac_vector_scalar(v, s, method_function):
    sv = [s]*len(v)
    __yearfrac_vector_vector(v, sv, method_function)


def __yearfrac_vector_vector(v1, v2, method_funciton):
    rows = zip(v1, v2)
    return [
        method_funciton(
            s1.year, s1.month, s1.day, s2.year, s2.month, s2.day
        )
        for s1, s2 in rows
    ]


__algorithm_mapper = {
        (True, True): __yearfrac_vector_vector,
        (False, False): __yearfrac_scalar_scalar,
        (True, False):
            lambda v, s, m: __yearfrac_vector_vector(v, [s]*len(v), m),
        (False, True):
            lambda s, v, m: __yearfrac_vector_vector([s]*len(v), v, m)
    }


def yearfrac(d1, d2, method='act'):
    yearfrac_func = __algorithm_mapper[
        (
            isinstance(d1, collections.Iterable),
            isinstance(d2, collections.Iterable)
        )
    ]
    method_function = __get_method_function(method)
    return yearfrac_func(d1, d2, method_function)
