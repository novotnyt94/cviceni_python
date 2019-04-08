def fibonacci(n=-1): #implementation for both fibo_gen and fibonacci
    i0 = 0
    i1 = 1
    # Hmm, that's devilishly clever!
    while True:
        #infinite loop support
        if n == 0:
            break
        n -= 1
        #return next element and compute a new one
        yield i1
        i0, i1 = i1, i0+i1
  
print(list(fibonacci(10)))

def fib(n):
    gen = fibonacci(n)
    try:
        while True:
            val = next(gen)
    except StopIteration:
        return val
        


print(fib(5))

