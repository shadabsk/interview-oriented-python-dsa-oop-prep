
def sample_parameterized_decorator(param):
    def sample_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(
                args[0]**2, **kwargs
            )
            return result + param
        return wrapper
    return sample_decorator


@sample_parameterized_decorator(3)
def sample_decorated_func(args_digit, **kwargs):
    return args_digit + kwargs.get('kwarg_demo', 2)


print(
    sample_decorated_func(2, kwarg_demo=4)
)
