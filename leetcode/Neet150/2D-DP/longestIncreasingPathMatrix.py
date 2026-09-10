from typing import List

# DP with memoization
# m -> len(matrix); n -> len(matrix[0])
# TC -> O(m * n)
# SC -> O(m * n)
# Approach
# DP state -> (row, col): max_increasing_len


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        dp = {}
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col):

            if (row, col) in dp:
                return dp[(row, col)]

            count = 1
            for r, c in dirs:
                next_r = row + r
                next_c = col + c
                if (
                        0 <= next_r < len(matrix)
                        and 0 <= next_c < len(matrix[0])
                        and matrix[next_r][next_c] > matrix[row][col]
                ):
                    count = max(1 + dfs(next_r, next_c), count)

            dp[(row, col)] = count
            return count

        mx = float('-inf')
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                mx = max(mx, dfs(r, c))

        return mx

if __name__ == "__main__":
    sln = Solution()
    matrix = [[5,5,3],[2,3,6],[1,1,1]]
    print(sln.longestIncreasingPath(matrix))