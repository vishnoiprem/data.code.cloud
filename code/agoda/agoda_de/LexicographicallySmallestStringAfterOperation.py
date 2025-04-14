
def smallestString(s):
    for i, c in enumerate(s):
        if c != 'a':
            break
    else:
        return s[:-1] + 'z'
    res = s[:i] + ''.join(chr(ord(c) - 1) if c != 'a' else c for c in s[i:])
    return res

# Example:
# Input: "abcz"
# Output: "abcy"
# Time Complexity: O(N)
# Space Complexity: O(N)
