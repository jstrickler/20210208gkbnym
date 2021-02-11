from functools import wraps
from datetime import datetime

def print_time_stamp(original_function):

    @wraps(original_function)
    def new_func(*args, **kwargs):
        timestamp = datetime.now().ctime()
        print(timestamp)
        return original_function(*args, **kwargs)

    return new_func

@print_time_stamp
def spam():
    print("Hello from spam()")

@print_time_stamp
def make_line(char, size):
    return char * size

spam()
spam()
print(make_line('*', 50))
print(make_line('-', 60))
