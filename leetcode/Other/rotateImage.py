from typing import List

# Approach:
# Use the formula to rotate a value in a matrix.
# elem_o -> order of the element; i = current idx of the element in the matrix; f_row, l_row -> idx of the first and
# last rows; l_row, f_col -> idx of the first and last cols.
# (f_row, i) -> (i, l_col) -> (l_row, l_col - elem_o) -> (l_row - elem_o, f_col)
# We should run the while and for loops only on the first row of the considered matrix (it can be either an outer matrix
# or an inner matrix). Once for loop is done -> shrink first/last rows and cols by 1 and restart the for loop on the
# inner matrix.

# TC -> O(n^2)
# SC -> O(1)

class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix) - 1
        f_row, f_col = 0, 0
        l_col, l_row = n, n

        while n > 0:
            elem_o = 0
            for i in range(f_col, n):
                top = matrix[f_row][i]
                right = matrix[i][l_col]
                bottom = matrix[l_row][l_col - elem_o]
                left = matrix[l_row - elem_o][f_col]

                # Modifications
                matrix[i][l_col] = top
                matrix[l_row][l_col - elem_o] = right
                matrix[l_row - elem_o][f_col] = bottom
                matrix[f_row][i] = left

                elem_o += 1

            n -= 1
            f_row += 1
            f_col += 1
            l_col, l_row = n, n