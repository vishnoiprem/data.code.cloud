#https://leetcode.com/problems/next-greater-element-i/description/
def nextGreaterElement(nums1, nums2):
    stack = []
    next_greater = {}
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)

    return [next_greater.get(num, -1) for num in nums1]


# Example usage
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2))  # Output: [-1, 3, -1]