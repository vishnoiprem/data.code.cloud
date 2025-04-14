def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        print(a)
        a, b = b, a + b
        count += 1

# Usage
for num in fibonacci(2):
    print(num)
