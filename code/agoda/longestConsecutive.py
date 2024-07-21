
# Simple Approach (O(n log n) Time Complexity)


#sort
#iterate through the array



def longestConsecutive_long(nums):

    if len(nums) <= 1:
        return len(nums)

    nums.sort()
    longest_streak = 1
    current_streak = 1

    for i in range(1,len(nums)):
        if nums[i] == nums[i-1] + 1:
            current_streak += 1
        else:
            longest_streak = max(longest_streak, current_streak)
            current_streak = 1

    return max(longest_streak, current_streak)
    # Example usage
nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive_long(nums))  # Output: 4 (sequence: [1, 2, 3, 4])

#Optimized Approach (O(n) Time Complexity)
def longestConsecutive(nums):

    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:  # start of a sequence
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


# Example usage
nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))  # Output: 4 (sequence: [1, 2, 3, 4])

