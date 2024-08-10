def largest_prime_factor(n):
    # Step 1: Divide n by 2 until it becomes odd
    while n % 2 == 0:
        n //= 2

    # If n becomes 1, it means 2 was the largest prime factor
    if n == 1:
        return 2

    # Step 2: Check for odd factors starting from 3
    largest_factor = 3
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            largest_factor = i
            n //= i

    # Step 3: If n is still greater than 2, then it is prime
    if n > 2:
        largest_factor = n

    return largest_factor


# Example usage:
n = 13195
print(largest_prime_factor(n))  # Output: 29

n2 = 600851475143
print(largest_prime_factor(n2))  # Output: 6857
