def fizz_buzz_sum(target):
    total_sum = 0
    for num in range(target):
        if num % 3 == 0 or num % 5 == 0:
            total_sum += num
    return total_sum

# Example usage:
target_value = 10
result = fizz_buzz_sum(target_value)
print(result)  # Output should be 23
