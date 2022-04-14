import time
from functools import wraps


def time_decorator(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(time.time() - start)

    return decorated
