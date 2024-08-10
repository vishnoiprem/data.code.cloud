# n, write a formula that returns


def factorial(n):

    if n == 1 or n==0:
        return 1
    # return n*factorial(n-1)
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result
n =5


def factorial_recursive(n):
    if n == 1 or n==0:
        return 1
    return n*factorial_recursive(n-1)
print(factorial(n))
print( factorial_recursive(n))