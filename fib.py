cache = {}


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        value = fib(n-1) + fib(n-2)
        cache[n] = value
        return value