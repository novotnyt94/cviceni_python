#Meta-class for the Struct task 
class custom_meta(type):
  #Restructualize given class to have slots instead of dict; redefine __init__ and __repr__
  def __new__(cls, name, bases, namespace):
    #all user-defined class attributes should be in slots
    slots = tuple(key for key, value in namespace.items() if not key.startswith('__'))
    #save original init (if defined) to be able to call it
    old_init = None
    if "__init__" in namespace:
      old_init = namespace["__init__"]
    #save default values of attributes to be able to check change 
    defaults = {key:namespace[key] for key in slots}
    #keep remaining attributes
    for key in slots: 
      del namespace[key]
    
    #custom init to initialize instance variables as desired
    def init(self, *args, **kwargs):
      #copy defaults
      for key, value in defaults.items():
        self.__setattr__(key, value)
      #overwrite rewuired attributes
      for key, value in kwargs.items():
        self.__setattr__(key, value)
      #run original init (if required)
      if old_init:
        old_init(self, *args, **kwargs)
    
    #string as in given task   
    def repr(self):
      result = name + "("
      first = True
      for key in self.__slots__:
        if self.__getattribute__(key) != defaults[key]: 
          if not first:
            result += ", "
          first = False
          result += key + "=" + str(self.__getattribute__(key))
      result += ")" 
      return result
    
    #add created items into namespace      
    namespace["__slots__"] = slots
    namespace["__init__"] = init
    namespace["__repr__"] = repr
    #send result into type
    return super().__new__(cls, name, bases, namespace)

#I don't know what this class should be good for...
class Struct(metaclass=custom_meta):
  pass             



##### Tests #####
if __name__ == "__main__": 
  class Point(Struct):
    x = 3.5
    y = 4.5 
  p = Point(y = 8)
  print(p) # prints Point(y=8) --value of x is not shown because it is the default one
  p.y = 2
  p.x = 3
  print(p) # prints Point(x=3, y=2) --both values are shown because neither is the same as the default
  p.y = 4.5
  print(p) # prints Point(x=3) --y was returned into default value
  # This causes the following error ... AttributeError: 'Point' object has no attribute 'z'
  #p.z = 3
    
  ### works also with custom init! ###
  class PointInit(Struct):
    def __init__(self, x_val):
      self.x = x_val
    x = 13.5
    y = 14.5
  
  pi = PointInit(42)
  print(pi) #prints PointInit(x=42)