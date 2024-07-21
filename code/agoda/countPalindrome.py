class Solution:
    def __init__(self):
        self.count = 0

    def countSubstrings(self, s: str) -> int:
        for i in range(len(s)):
            self.countPalindrome(s, i, i)  # Odd length palindromes
            self.countPalindrome(s, i, i + 1)  # Even length palindromes
        return self.count

    def countPalindrome(self, s: str, l: int, r: int) -> None:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            self.count += 1
            l -= 1
            r += 1


# Example usage
s = "aaa"
solution = Solution()
print(solution.countSubstrings(s))  # Output: 6