from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Step 1: Sort the intervals by the starting point
        intervals.sort(key=lambda x: x[0])

        # Step 2: Initialize the merged intervals list with the first interval
        merged_intervals = [intervals[0]]

        # Step 3: Iterate through the sorted intervals
        for current_interval in intervals[1:]:
            last_merged_interval = merged_intervals[-1]

            # If the current interval overlaps with the last merged interval, merge them
            if current_interval[0] <= last_merged_interval[1]:
                last_merged_interval[1] = max(last_merged_interval[1], current_interval[1])
            else:
                # Otherwise, add the current interval to the merged list
                merged_intervals.append(current_interval)

        return merged_intervals

# Example usage
sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))  # Output: [[1,6],[8,10],[15,18]]
print(sol.merge([[1,4],[4,5]]))  # Output: [[1,5]]


