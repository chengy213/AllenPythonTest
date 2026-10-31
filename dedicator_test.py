import functools
import time

def log(func):
    def wrapper(*args, **kwargs):
        print(f"call {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def metric(text):
    def dedictor(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{text}->start call {func.__name__}")
            start=time.time()
            r=func(*args, **kwargs)
            end=time.time()
            cost=end-start
            print(f"{text}->end call {func.__name__}, cost time:{cost}")
            return r
        return wrapper
    return dedictor

@metric("execute")
def current_month():
    time.sleep(1.5)
    print(time.localtime())

print(current_month())