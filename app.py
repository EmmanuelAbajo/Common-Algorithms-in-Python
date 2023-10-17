def factorial(n):
    if (n < 1): return -1
    if (n==1 or n==0): return 1
    return n * factorial(n-1)

# Naive recursive approach
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Top down approach
def fibonacci_td(n, cache={}):
    if n <= 1:
        return n
    
    if n in cache:
        return cache[n]
    
    cache[n] = fibonacci_td(n-1, cache) + fibonacci_td(n-2, cache)
    return cache[n]    

# Bottom top approach
def fibonacci_bt(n):
    if n <= 1:
        return n
    f = [-1] * n
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]    

if __name__ == '__main__':
    v = factorial(20)
    print('Factorial of 20: ',v)