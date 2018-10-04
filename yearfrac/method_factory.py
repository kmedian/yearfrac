from .act_isda import act_isda
from .act_afb import act_afb
from .d30360e import d30360e
from .d30365 import d30365

# Add new method calls here.
# The default signature is function_name(x1, x2, x3, y1, y2, y3).
# If there are more input arguments, use lambda expressions
# or define a function wrapper.

methods = dict.fromkeys(['act', 'act_afb', 'afb'], act_afb)
methods.update(
    dict.fromkeys(
        ['d30360e', '30e360'],
        lambda x1, x2, x3, y1, y2, y3: d30360e(
            x1, x2, x3,
            y1, y2, y3,
            False
        )
    )
)
methods.update({'act_isda': act_isda})
methods.update(
    dict.fromkeys(
        ['d30360e_matu', '30e360_matu'],
        lambda x1, x2, x3, y1, y2, y3: d30360e(
            x1, x2, x3,
            y1, y2, y3,
            True
        )
    )
)
methods.update({'30365': d30365})
