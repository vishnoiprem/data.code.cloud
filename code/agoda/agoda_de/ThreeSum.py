def threeSum(nums):
    nums.sort()  # Sort the array to handle duplicates and use two pointers
    res = []

    for i in range(len(nums) - 2):
        # Skip duplicate elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Two pointers initialization
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:  # Found a triplet
                res.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for left and right pointers
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move both pointers
                left += 1
                right -= 1
            elif total < 0:
                left += 1  # We need a larger sum, move the left pointer
            else:
                right -= 1  # We need a smaller sum, move the right pointer

    return res


# Example Usage:
nums = [-1, 0, 1, 2, -1, -4]
# Running the function
triplets = threeSum(nums)
print(f"Triplets that sum up to zero: {triplets}")