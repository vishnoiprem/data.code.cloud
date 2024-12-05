
def longestPalindrome(s):
    if not s:
        return ""

    start, end = 0, 0
    for i in range(len(s)):
        len1 = expandFromCenter(s, i, i)
        len2 = expandFromCenter(s, i, i + 1)
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    return s[start:end + 1]

def expandFromCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

# Example:
# Input: "babad"
# Output: "bab"
# Time Complexity: O(N^2)
# Space Complexity: O(1)
