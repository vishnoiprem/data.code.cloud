def int_str_addition(int_str):
    total_sum = 0

    # Get all possible substrings of the input string
    n = len(int_str)
    for i in range(n):
        for j in range(i + 1, n + 1):
            # Convert the substring to integer and add it to the total sum
            total_sum += int(int_str[i:j])

    return total_sum


# Example Usage:
int_str = '123'
print(int_str_addition(int_str))  # Output: 164
print(int_str_addition('12'))  # Output: 164