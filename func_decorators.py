#simple decorator
def ignore_errors(func, ret=None):
    def inner(*args):
        try:
            return func(*args)
        except:
            return ret
    return inner

@ignore_errors
def divide(a, b):
    return a/b

print(divide(1,1))
print(divide(1,0))

#decorator with arg
def ignore_errors_arg(ret=None):
    def ignore_errors(func):
        def inner(*args):
            try:
                return func(*args)
            except:
                return ret
        return inner
    return ignore_errors

@ignore_errors_arg(ret=24)
def divide2(a, b):
    return a/b
    
print(divide2(1,1))
print(divide2(1,0))

#alternative solution with partial
from functools import partial
def ignore_errors_arg2(ret=None):
    return partial(ignore_errors, ret=ret)
    
@ignore_errors_arg2(ret=42)
def divide3(a, b):
    return a/b
    
print(divide3(1,1))
print(divide3(1,0))
