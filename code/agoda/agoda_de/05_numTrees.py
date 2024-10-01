def numTrees(n):
    # Base case: for 0 nodes or 1 node, there's only one unique BST.
    if n == 0 or n == 1:
        return 1

    # Create a list to store the number of unique BSTs for each count up to n.
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1  # G(0) = 1, G(1) = 1

    # Fill the dp array using the formula G(n) = sum(G(i-1) * G(n-i))
    for nodes in range(2, n + 1):
        total_trees = 0
        for root in range(1, nodes + 1):
            left_trees = dp[root - 1]  # Number of unique BSTs in the left subtree
            right_trees = dp[nodes - root]  # Number of unique BSTs in the right subtree
            total_trees += left_trees * right_trees

        dp[nodes] = total_trees

    # Return the number of unique BSTs for n nodes
    return dp[n]

# Example usage:
print(numTrees(3))  # Output: 5
print(numTrees(1))  # Output: 1