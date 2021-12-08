import functools
import time


def profile_with_message(msg): # return decorator with parameter msg available
    def profile(f):            # decorates f
        @functools.wraps(f)
        def wrapper(*args, **kwargs):   # wrapper code
            # something before
            start = time.time()
            result = f(*args, **kwargs)  # call f
            # something after
            end = time.time()
            print(msg, end - start)
            return result
        return wrapper
    return profile


def retry(times, start_wait=0.1):
    def internal(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            wait = start_wait
            for i in range(times-1):
                try:
                    return f(*args, **kwargs)
                except:
                    print(f'wait {wait} seconds')
                    time.sleep(wait)
                    wait *= 2
            return f(*args, **kwargs)
        return wrapper
    return internal


def cache(f):
    cache_obj = {}

    @functools.wraps(f)
    def wrapper(*args):
        if args not in cache_obj:
            print('calculate', args)
            cache_obj[args] = f(*args)
        else:
            print('from cache', args)
        return cache_obj[args]

    return wrapper


@retry(4)
@cache
@profile_with_message("Elapsed time: ")
def triangle(n):
    return sum(range(n+1))


result = triangle(10)
print("Result", result)