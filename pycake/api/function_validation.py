from functools import wraps as _wraps


def _must_have_one(param_list):
    def actual_decorator(f):
        @_wraps(f)
        def wrapper(*args, **kwargs):
            if not any(i in kwargs for i in param_list):
                raise Exception('Please provide one of the following: '
                    '{}'. format(', '.join(param_list)))
            else:
                return f(*args, **kwargs)
        return wrapper
    return actual_decorator

def _if_one_then_all(param_list):
    def actual_decorator(f):
        @_wraps(f)
        def wrapper(*args, **kwargs):
            for param in param_list:
                if (param in kwargs and not
                        all(param in kwargs for param in param_list)):
                    raise Exception('If providing one of the following '
                        'please provide all: {}'.format(
                        ', '.join(param_list)))
            else:
                return f(*args, **kwargs)
        return wrapper
    return actual_decorator