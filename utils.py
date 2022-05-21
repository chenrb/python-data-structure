import time
from functools import wraps


def time_decorator(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("cost time: %s" % (time.time() - start))
        return result

    return decorated
