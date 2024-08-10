class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = 0
        for char in s:
            result ^= ord(char)
            print(result)
        for char in t:
            result ^= ord(char)
        return chr(result)

# Example usage
sol = Solution()
print(sol.findTheDifference("abcd", "abcde"))  # Output: "e"
print(sol.findTheDifference("", "y"))  # Output: "y"