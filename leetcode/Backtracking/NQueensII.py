
# TC -> O(n!)
# SC -> O(n)

# Approach:
# Maintain 3 sets, each one of them will be responsible for maintaining coordinates, on a respective line,
# which are prohibited to use. Specifically, we would want to separately store rows, upper
# diagonals and lower diagonals that are prohibited.
# Use a recursive function - 'dfs()', which will check each queen placement per col. If queen placement on a particular
# row is not allowed (row is captured, current_row - current_col (upper diagonal is captured) or current_row + current_col
# (lower diagonal is captured)), then it's skipped, otherwise we are populating 3 sets accordingly.

# If we were able to reach the bottom of the recursion -> res += 1

# On return from the dfs() function, we backtrack by removing taken diagonal coordinates and removing taken rows from
# the respective sets.

class Solution:
    def totalNQueens(self, n: int) -> int:
        p_upper_diagonal = set()
        p_row = set()
        p_lower_diagonal = set()

        res = 0

        def dfs(col):
            if col >= n:
                nonlocal res
                res += 1
                return

            for i in range(n):

                if (
                        i not in p_row
                        and i - col not in p_upper_diagonal
                        and i + col not in p_lower_diagonal
                ):
                    p_row.add(i)

                    n_upper = i - col
                    p_upper_diagonal.add(n_upper)

                    n_lower = i + col
                    p_lower_diagonal.add(n_lower)

                    dfs(col + 1)

                    # backtrack
                    p_upper_diagonal.remove(n_upper)
                    p_lower_diagonal.remove(n_lower)
                    p_row.remove(i)

        dfs(0)
        return res


if __name__ == "__main__":
    sln = Solution()
    sln.totalNQueens(4)
