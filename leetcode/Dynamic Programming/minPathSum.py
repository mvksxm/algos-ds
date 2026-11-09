
# R -> rows
# C -> cols

# Recursive DP solution
# TC -> O(R * C)
# SC -> O(R * C)

# Iterative DP solution
# TC -> O(R * C)
# SC -> O(1) (input grid is reused for the answer)


class Solution:

    # Recursive DP solution
    def minPathSumRecursive(self, grid: list[list[int]]) -> int:

        # state -> (row, col)
        dp = {}
        dirs = [(0, 1), (1, 0)]


        def dfs(r, c):

            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return grid[r][c]

            if (r, c) in dp:
                return dp[(r, c)]

            min_child = float('inf')

            for (m_r, m_c) in dirs:
                n_r, n_c = r + m_r, c + m_c
                if (
                        0 <= n_r < len(grid)
                        and 0 <= n_c < len(grid[0])
                ):
                    min_child = min(min_child, dfs(n_r, n_c))

            local_sm = grid[r][c] + min_child
            dp[(r, c)] = local_sm
            return local_sm

        return dfs(0, 0)

    # Iterative DP solution
    def minPathSum(self, grid: list[list[int]]) -> int:

        cols = len(grid[0])

        # Populate last row
        for i in range(len(grid[0]) - 2, -1, -1):
            grid[-1][i] = grid[-1][i] + grid[-1][i + 1]

        # Populate last col
        for i in range(len(grid) - 2, -1, -1):
            grid[i][cols - 1] = grid[i][cols - 1] + grid[i + 1][cols - 1]

        # Main loop
        for i in range(len(grid) - 2, -1, -1):
            for j in range(len(grid[0]) - 2, -1, -1):
                grid[i][j] = grid[i][j] + min(grid[i][j + 1], grid[i + 1][j])


        return grid[0][0]

if __name__ == "__main__":
    sln = Solution()
    print(sln.minPathSum([[1,2,3],[4,5,6]]))