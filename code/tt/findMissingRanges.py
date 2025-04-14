from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []
        nums.append(upper + 1)  # Sentinel value to handle the last range
        prev = lower - 1

        for num in nums:
            if num - prev > 1:
                if prev + 1 == num - 1:
                    result.append([prev + 1, prev + 1])
                else:
                    result.append([prev + 1, num - 1])
            prev = num

        return result


nums = [0,1,3,50,75]
lower = 0
upper = 99
sol = Solution()
print(sol.findMissingRanges(nums, lower, upper))  # Output: [[2, 2], [4, 49], [51, 74], [76, 99]]
