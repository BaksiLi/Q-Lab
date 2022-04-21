import functools
import inspect
import warnings


def _deprecated(reason: str):
    """Decorator for deprecated functions/classes.

    Example
    @deprecated('use print_a instead.')
    def printA():
        print('A')
    """

    if isinstance(reason, str):

        def decorator(func1):

            if inspect.isclass(func1):
                fmt1 = "Call to deprecated class {name} ({reason})."
            else:
                fmt1 = "Call to deprecated function {name} ({reason})."

            @functools.wraps(func1)
            def new_func1(*args, **kwargs):
                warnings.simplefilter('always', DeprecationWarning)
                warnings.warn(fmt1.format(name=func1.__name__, reason=reason),
                              category=DeprecationWarning,
                              stacklevel=2)
                warnings.simplefilter('default', DeprecationWarning)
                return func1(*args, **kwargs)

            return new_func1

        return decorator

    # if no reasons is given
    elif inspect.isclass(reason) or inspect.isfunction(reason):
        func2 = reason

        if inspect.isclass(func2):
            fmt2 = "Call to deprecated class {name}."
        else:
            fmt2 = "Call to deprecated function {name}."

        @functools.wraps(func2)
        def new_func2(*args, **kwargs):
            warnings.simplefilter('always', DeprecationWarning)
            warnings.warn(fmt2.format(name=func2.__name__),
                          category=DeprecationWarning,
                          stacklevel=2)
            warnings.simplefilter('default', DeprecationWarning)
            return func2(*args, **kwargs)

        return new_func2

    else:
        raise TypeError(repr(type(reason)))
