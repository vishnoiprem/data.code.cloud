
def kthSmallest(root, k):
    def inorder(node):
        return inorder(node.left) + [node.val] + inorder(node.right) if node else []
    return inorder(root)[k - 1]

# Example:
# Input: [3,1,4,null,2], k = 1
# Output: 1
# Time Complexity: O(N)
# Space Complexity: O(N)
