
def firstUniqChar(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1

# Example:
# Input: "loveleetcode"
# Output: 2
# Time Complexity: O(N)
# Space Complexity: O(1)
