class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            mid = left + (right - left) // 2
            num = mid * mid

            if num == x:
                return mid
            elif num < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


# Example usage
sol = Solution()
print(sol.mySqrt(4))  # Output: 2
print(sol.mySqrt(8))  # Output: 2
