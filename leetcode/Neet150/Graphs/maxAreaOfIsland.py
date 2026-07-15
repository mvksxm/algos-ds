# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

class Solution:
    def maxAreaOfIsland(self, grid: list) -> int:

        max_area = 0
        def _dfs(row, col) -> int:

            if row > len(grid) - 1 or row < 0:
                return 0

            if col > len(grid[0]) - 1 or col < 0:
                return 0

            if grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            land_sum = _dfs(row - 1, col) + _dfs(row, col + 1) + _dfs(row + 1, col) + _dfs(row, col - 1) + 1
            return land_sum


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    max_area = max(_dfs(row, col), max_area)

        return max_area


if __name__ == "__main__":
    sln = Solution()
    grid=[[0,1,1,0,1],[1,0,1,0,1],[0,1,1,0,1],[0,1,0,0,1]]
    print(sln.maxAreaOfIsland(grid))