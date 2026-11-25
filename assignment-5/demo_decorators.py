from functools import wraps
import time


def log_call(label):
    """prints args and return value for any decorated function"""
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"[{label}] called with {args}")
            out = fn(*args, **kwargs)
            print(f"[{label}] returned {out}")
            return out
        return wrapper
    return decorator


def timer(fn):
    """measures how long a function takes to run"""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = fn(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        print(f"  {fn.__name__} took {elapsed:.6f}s")
        return result
    return wrapper


@log_call("add")
def add(a, b):
    return a + b


@log_call("sub")
def subtract(a, b):
    return a - b


@log_call("mul")
def multiply(a, b):
    return a * b


@timer
@log_call("pow")
def power(base, exp):
    return base ** exp


print("--- basic operations ---")
add(10, 5)
add(42, 8)
subtract(100, 37)
multiply(6, 7)

print("\n--- power with timer ---")
power(2, 10)
power(3, 20)
