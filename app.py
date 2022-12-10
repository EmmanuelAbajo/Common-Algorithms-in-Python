def factorial(n):
    if (n < 1): return -1
    if (n==1 or n==0): return 1
    return n * factorial(n-1)

def fibonacci(n):
    pass

if __name__ == '__main__':
    v = factorial(20)
    print('Factorial of 20: ',v)