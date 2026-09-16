
# m -> len(matrix); n -> len(matrix[0])
# TC -> O(m * n)
# SC -> O(1)

# Approach
# Mask 0s with None. Then perform iteration on rows, where, in case if None is encountered all non-None values are
# modified to 0. Right after, perform iteration on cols, in case if None is encountered -> modify all values in a col
# to 0.

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Change 0s to None
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0: matrix[r][c] = None

        # Row Iteration
        for r in range(len(matrix)):

            # Search 0
            zero_found = False
            for c in range(len(matrix[r])):
                if matrix[r][c] is None:
                    zero_found = True
                    break

            if zero_found:
                for c in range(len(matrix[r])):
                    if matrix[r][c] is not None: matrix[r][c] = 0

        # Column Iteration
        for c in range(len(matrix[0])):

            zero_found = False
            for r in range(len(matrix)):
                if matrix[r][c] is None:
                    zero_found = True
                    break

            if zero_found:
                for r in range(len(matrix)):
                    matrix[r][c] = 0