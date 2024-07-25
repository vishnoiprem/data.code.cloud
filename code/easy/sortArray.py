# Here’s a step-by-step plan and the implementation in Python:
#
# Step-by-Step Plan:
# https://leetcode.com/problems/sort-an-array/?envType=daily-question&envId=2024-07-25
# 	1.	Divide: Split the array into two halves until each subarray contains a single element.
# 	2.	Conquer: Recursively sort each subarray.
# 	3.	Combine: Merge the sorted subarrays to produce the sorted array.


from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr: List[int]) -> List[int]:
            if len(arr) > 1:
                mid = len(arr) // 2
                L = arr[:mid]
                R = arr[mid:]

                merge_sort(L)
                merge_sort(R)

                i = j = k = 0

                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1

                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1

                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1

            return arr

        return merge_sort(nums)


# Example usage:
solution = Solution()
nums1 = [5, 2, 3, 1]
nums2 = [5, 1, 1, 2, 0, 0]

print(solution.sortArray(nums1))  # Output: [1, 2, 3, 5]
print(solution.sortArray(nums2))  # Output: [0, 0, 1, 1, 2, 5]

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(0, n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]  # Swap the elements
        return nums

# Example usage:
solution = Solution()
nums1 = [5, 2, 3, 1]
nums2 = [5, 1, 1, 2, 0, 0]

print(solution.sortArray(nums1))  # Output: [1, 2, 3, 5]
print(solution.sortArray(nums2))  # Output: [0, 0, 1, 1, 2, 5]