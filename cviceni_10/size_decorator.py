# Feedback:
#
#     + Correct implementation.
#     + Well commented. (Better use """function comment""" to document your code.)
#     + __name__ == "__main__"
#     - Please use four spaces to format you code!
#     - Please use hashbang.
#
# The rest of the comments is inlined (look for Feedback:).

#Decorator returning required descriptor
def size(all_instances):
  def inner(function):
    #returns instance of descriptor providing value over required instance(s)
    return CustomDescriptor(function, all_instances)
  return inner

#Descriptor, which returns value of:
# - given function if called on instance
# - sum of calls of given function over all available instances
class CustomDescriptor:
  def __init__(self, function, all_instances):
    self.function = function
    self.all_instances = all_instances
    
  def __get__(self, instance, owner):
    # Feedback: "if instance" is enough, no need to test against None.
    if instance != None:
      return self.function(instance)
    else: # Feedback: else is unnecessary here.
      #run function over provided instances and sum the result
      values = [self.function(inst) for inst in self.all_instances()]
      return sum(values)
  


###test ze slidu###
if __name__ == "__main__": 
  class Cache:
    def __init__(self):
      Cache._all_caches.append(self)
      self._storage= dict()
      
    _all_caches = []
    
    def set(self, key, value):
      self._storage[key] = value
    def get(self, key):
      self._storage[key]
    def _all_instances():
      return Cache._all_caches
      
    @size(all_instances=_all_instances)
    def entries_count(self):
      return len(self._storage)
  
         
  a = Cache()
  b = Cache()
  
  a.set("a", 1)
  a.set("b", 2)
  b.set("c", 3)
  
  print(a.entries_count)      # prints 2
  print(b.entries_count)      # prints 1
  print(Cache.entries_count)  # prints 3
        
