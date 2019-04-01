def my_map(arr, func):
    for elem in arr:
        yield(func(elem))
        
  
def invert(string):
    return string[::-1]
    
test_str = ["one", "two", "three"]

print(list(my_map(test_str, invert)))
