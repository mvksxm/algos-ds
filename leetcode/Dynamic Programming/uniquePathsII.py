
# TC -> O(m*n)
# SC -> O(1)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

        if obstacleGrid[-1][-1] == 1: return 0

        obstacleGrid[-1][-1] = 1

        for row in range(len(obstacleGrid) - 1, -1, -1):
            for col in range(len(obstacleGrid[row]) - 1, -1, -1):
                if obstacleGrid[row][col] == 1 and not (row == len(obstacleGrid) - 1 and col == len(obstacleGrid[0]) - 1):
                    obstacleGrid[row][col] = 0
                    continue

                bottom_val = obstacleGrid[row + 1][col] if row + 1 < len(obstacleGrid) else 0
                right_val = obstacleGrid[row][col + 1] if col + 1 < len(obstacleGrid[0]) else 0
                obstacleGrid[row][col] = bottom_val + right_val + obstacleGrid[row][col]

        return obstacleGrid[0][0]

if __name__ == "__main__":
    sln = Solution()
    obstacleGrid = [[0, 1], [0, 0]]
    print(sln.uniquePathsWithObstacles(obstacleGrid))