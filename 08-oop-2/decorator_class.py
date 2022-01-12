import functools
import time


class cache_for_time:
    def __init__(self, seconds):
        self.seconds = seconds
        self.cache_obj = {}
        self.cache_time = {}

    def __call__(self, f):
        @functools.wraps(f)
        def wrapper(*args):
            if args not in self.cache_obj or self.cache_time[args] < time.time() - self.seconds:
                print('calculate', args)
                self.cache_obj[args] = f(*args)
                self.cache_time[args] = time.time()
            else:
                print('from cache', args)
            return self.cache_obj[args]

        return wrapper


@cache_for_time(1)
def triangle(a):
    return a * (a + 1) // 2


r = triangle(3)
print(r)

r = triangle(3)
print(r)

time.sleep(2)
r = triangle(3)
print(r)