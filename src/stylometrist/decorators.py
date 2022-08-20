from typing import Callable
from functools import wraps

from .common import Text, registry


def measurement(f: Callable) -> Callable:
    """ Logs measurement to registry and converts text as str to Text instance """

    @wraps(f)  # For some unknown reason, this makes Sphinx automodule work on a decorated function
    def wrapper(*args, **kw):
        registry[f.__name__] = {'function': f}

        try:
            text = kw['text']
            start_arg = 0
        except KeyError:
            text = args[0]
            start_arg = 1

        if not isinstance(text, Text):
            kw['text'] = Text(str(text))

        return f(*args[start_arg:], **kw)

    return wrapper
