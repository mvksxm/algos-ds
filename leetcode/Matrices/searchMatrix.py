from typing import List


# TC -> O(n + m)
# SC -> O(1)

class Solution:


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        r = 0
        c = len(matrix[0]) - 1

        while 0 <= r < rows and 0 <= c < cols:

            next_col = -1
            i = c
            while i >= 0:

                if matrix[r][i] == target: return True

                if matrix[r][i] < target:
                    next_col = i
                    break

                i -= 1

            if next_col == -1: return False

            c = next_col
            r += 1
            next_row = rows

            i = r
            while i < rows:

                if matrix[i][c] == target: return True

                if matrix[i][c] > target:
                    next_row = i
                    break

                i += 1

            if next_row == rows: return False

            c -= 1
            r = next_row

        return False

if __name__ == "__main__":
    sln = Solution()
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 20
    print(sln.searchMatrix(matrix, target))
