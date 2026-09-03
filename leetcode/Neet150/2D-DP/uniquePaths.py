
# TC -> O(m * n)
# SC -> O(m * n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}

        def dfs(coordinates):
            r, c = coordinates

            if r == m - 1 and c == n - 1:
                return 1

            if r >= m or c >= n:
                return 0

            if (r, c) in dp:
                return dp[(r, c)]

            sm = dfs((r+1, c)) + dfs((r, c+1))
            dp[(r, c)] = sm
            return sm

        return dfs((0, 0))