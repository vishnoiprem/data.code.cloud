from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # Step 1: Count the total number of 1's in the array
        count_ones = sum(data)

        # If there are no 1's or only one 1, no swaps are needed
        if count_ones <= 1:
            return 0

        # Step 2: Initialize the first window of size count_ones
        current_zero_count = count_ones - sum(data[:count_ones])
        print(current_zero_count,count_ones,sum(data[:count_ones]),data)
        min_swaps = current_zero_count

        # Step 3: Slide the window across the array
        for i in range(count_ones, len(data)):
            # Update the zero count by sliding the window
            if data[i - count_ones] == 0:
                current_zero_count -= 1
            if data[i] == 0:
                current_zero_count += 1

            # Track the minimum swaps needed
            min_swaps = min(min_swaps, current_zero_count)

        return min_swaps


# Example usage
sol = Solution()
print(sol.minSwaps([1, 0, 1, 0, 1]))  # Output: 1
print(sol.minSwaps([0, 0, 0, 1, 0]))  # Output: 0
print(sol.minSwaps([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]))  # Output: 3
