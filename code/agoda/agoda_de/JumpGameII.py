
def jump(nums):
    jumps = 0
    cur_end = 0
    cur_farthest = 0
    for i in range(len(nums) - 1):
        cur_farthest = max(cur_farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = cur_farthest
    return jumps

# Example:
# Input: [2,3,1,1,4]
# Output: 2
# Time Complexity: O(N)
# Space Complexity: O(1)
