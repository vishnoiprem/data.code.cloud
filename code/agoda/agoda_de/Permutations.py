
def permute(nums):
    res = []
    backtrack(nums, [], res)
    return res

def backtrack(nums, path, res):
    if not nums:
        res.append(path)
        return
    for i in range(len(nums)):
        backtrack(nums[:i] + nums[i + 1:], path + [nums[i]], res)

# Example:
# Input: [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Time Complexity: O(N * N!)
# Space Complexity: O(N * N!)
