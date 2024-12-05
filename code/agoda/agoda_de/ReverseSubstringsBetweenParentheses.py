
def reverseParentheses(s):
    stack = []
    for char in s:
        if char == ')':
            temp = []
            while stack and stack[-1] != '(':
                temp.append(stack.pop())
            stack.pop()  # Remove '('
            stack.extend(temp)
        else:
            stack.append(char)
    return ''.join(stack)

# Example:
# Input: "(u(love)i)"
# Output: "iloveu"
# Time Complexity: O(N)
# Space Complexity: O(N)
