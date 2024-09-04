from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(r, c):
            # If we are out of bounds or at a water cell ('0'), return
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
                return

            # Mark the cell as visited by setting it to '0'
            grid[r][c] = '0'

            # Explore the neighboring cells in all four directions
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        num_islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    # Found a new island, increment the count
                    num_islands += 1
                    # Use DFS to mark all the cells in this island
                    dfs(r, c)

        return num_islands


# Example usage
sol = Solution()
grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(sol.numIslands(grid1))  # Output: 1
print(sol.numIslands(grid2))  # Output: 3
