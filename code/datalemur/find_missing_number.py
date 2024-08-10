def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Example usage:
input_list = [0, 1, 3]
result = find_missing_number(input_list)
print(result)  # Output: 2

input_list2 = [4, 3, 2, 1]
result2 = find_missing_number(input_list2)
print(result2)  # Output: 0
