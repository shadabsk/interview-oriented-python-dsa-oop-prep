'''
Demo complete decorator pattern with its use cases in python
'''


def sample_decorated_func(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@sample_decorated_func
def sample_decorated_func(sample_input_str):
    return sample_input_str


sample_input_str = 'shadabsk'
print(
    sample_decorated_func(sample_input_str)
)
