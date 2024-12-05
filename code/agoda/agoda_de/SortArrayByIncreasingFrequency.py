
from collections import Counter

def frequencySort(nums):
    count = Counter(nums)
    return sorted(nums, key=lambda x: (count[x], -x))

# Example:
# Input: [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Time Complexity: O(N log N)
# Space Complexity: O(N)
