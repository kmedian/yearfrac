
import datetime
from .act_isda import act_isda
from .act_afb import act_afb
from .d30360e import d30360e
from .d30365 import d30365


def yearfrac(d1, d2, method='act'):
    if not isinstance(d1, (datetime.datetime, datetime.date)):
        raise Exception("d1 is not a datetime object.")

    if not isinstance(d2, (datetime.datetime, datetime.date)):
        raise Exception("d2 is not a datetime object.")

    if method.lower() in ('act', 'act_afb', 'afb'):
        return act_afb(
            d1.year, d1.month, d1.day,
            d2.year, d2.month, d2.day)
    elif method.lower() in ('act_isda'):
        return act_isda(
            d1.year, d1.month, d1.day,
            d2.year, d2.month, d2.day)
    elif method.lower() in ('d30360e', '30e360'):
        return d30360e(
            d1.year, d1.month, d1.day,
            d2.year, d2.month, d2.day,
            False)
    elif method.lower() in ('d30360e_matu', '30e360_matu'):
        return d30360e(
            d1.year, d1.month, d1.day,
            d2.year, d2.month, d2.day,
            True)
    elif method.lower() in ('30365'):
        return d30365(
            d1.year, d1.month, d1.day,
            d2.year, d2.month, d2.day)
    else:
        raise Exception("no method {0:s}".format(method))
