from src.stylib.common import Text, registry


def measurement(f):
    def wrapper(*args, **kw):
        registry[f.__name__] = f
        start_arg = 0
        try:
            text = kw['text']
        except KeyError:
            text = args[0]
            start_arg = 1
        if not isinstance(text, Text):
            kw['text'] = Text(str(text))
        return f(*args[start_arg:], **kw)

    return wrapper
