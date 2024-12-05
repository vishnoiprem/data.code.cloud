
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


print(permute([1, 2, 3]))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(permute([0, 1]))     # Output: [[0, 1], [1, 0]]
print(permute([1]))        # Output: [[1]]


def permute(nums):
    # Start with an empty list of permutations
    permutations = [[]]

    # Iterate over each number in the input list
    for num in nums:
        # Create a new list to store the updated permutations
        new_permutations = []

        # Iterate over each existing permutation
        for perm in permutations:
            # Insert the current number at every possible position
            for i in range(len(perm) + 1):
                # Create a new permutation with `num` inserted at position `i`
                new_permutations.append(perm[:i] + [num] + perm[i:])

        # Update permutations list to the newly generated permutations
        permutations = new_permutations

    return permutations


# Example usage
print(permute([1, 2, 3]))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(permute([0, 1]))  # Output: [[0, 1], [1, 0]]
print(permute([1]))  # Output: [[1]]
