def my_range(start, limit=None, step=1):
    #swap start-end, if both are given
    if limit == None:
        limit = start
        start = 0
        
    curr = start
    #handle negative step
    sign = 1
    if step < 0:
        sign = -1
    #generate next value
    while sign*curr < sign*limit:
        yield curr
        curr += step

print(list(my_range(5)))
print(list(my_range(8,15)))
print(list(my_range(22,0,-3)))
print(list(my_range(8,15,2)))

