# Agoda || Online || Permutation
# Question Link : https://leetcode.com/problems/permutations/
#
# Example test case :
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


import itertools


def permute_algo(nums):

    print( list(itertools.permutations(nums)))
    #TIME(O)=O(factor n)
    #SPACE(O)=O(factor n *n )

    return list(itertools.permutations(nums))

# Example test case
nums = [1, 2, 3]
print(permute_algo(nums))


def permute(nums):
    def backtrack(path, used):
        # If the current permutation is complete, add a copy of it to the results
        if len(path) == len(nums):
            results.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            # Add nums[i] to the current path
            path.append(nums[i])
            used[i] = True
            # Recursively build the permutation
            backtrack(path, used)
            # Backtrack by removing the last added element
            path.pop()
            used[i] = False

    results = []
    used = [False] * len(nums)
    backtrack([], used)
    return results

# Example test case


def permute1(nums):
    def backtrack(start=0):
        # If the current permutation is complete, add a copy of it to the results
        if start == len(nums):
            results.append(nums[:])
            return

        for i in range(start, len(nums)):
            # Place i-th integer first in the current permutation
            nums[start], nums[i] = nums[i], nums[start]
            # Use recursion to permute the rest of the array
            backtrack(start + 1)
            # Backtrack
            nums[start], nums[i] = nums[i], nums[start]

    results = []
    backtrack()
    return results


# Example test case
nums = [1, 2, 3]
print(permute1(nums))

nums = [1, 2, 3]
print(permute(nums))

nums = [1, 2, 3]
print(permute_algo(nums))