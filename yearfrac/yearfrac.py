
import datetime
from .act_isda import act_isda
from .act_afb import act_afb


def yearfrac(d1, d2, method='act'):
    if not isinstance(d1, (datetime.datetime, datetime.date)):
        raise Exception("d1 is not a datetime object.")

    if not isinstance(d2, (datetime.datetime, datetime.date)):
        raise Exception("d2 is not a datetime object.")

    if method in ('act_afb', 'act'):
        return act_afb(d1.year, d1.month, d1.day, d2.year, d2.month, d2.day)
    elif method in ('act_isda'):
        return act_isda(d1.year, d1.month, d1.day, d2.year, d2.month, d2.day)
    else:
        raise Exception("no method {0:s}".format(method))
