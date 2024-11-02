import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        elapsed_time_nanoseconds = end_time - start_time
        elapsed_time_microseconds = elapsed_time_nanoseconds * 1000
        
        return result, elapsed_time_microseconds, elapsed_time_nanoseconds
    return wrapper