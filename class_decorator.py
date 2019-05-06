import inspect
#simple decorator
def ignore_errors(func, ret=None):
    def inner(*args):
        try:
            return func(*args)
        except ValueError:
            return ret
    return inner

def class_decorator(source_class):
    #modifying function decorator
    def modify(func):
        def inner(*args):
            print("Method entry " + func.__name__)
            ret = func(*args)
            print("Method exit " + func.__name__)
            return ret
        return inner        
    
    #copy members    
    for member_name, member in inspect.getmembers(source_class):
        if member_name[0] != "_" and callable(member): #modify required members
            setattr(source_class, member_name, modify(member))  
            #eval("source_class." + member_name + " = member")
    return source_class

@class_decorator
class my_class:
    def __init__(self):
        super().__init__()
    def some_func(self, a, b, c):
        return a+b*c
    value = 1

#tests:    
mc = my_class()
print(mc.some_func(1,2,3)) #modified
print(mc.value)            #unmodified
print(mc.__repr__())       #unmodified
    

        
