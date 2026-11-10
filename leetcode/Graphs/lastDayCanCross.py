
# R -> rows
# C -> cols

# TC -> O(R * C)
# SC -> O(R * C)

class DSU:
    def __init__(self, n, row, col):
        self.top_flag = [False] * (n + 1)
        self.bottom_flag = [False] * (n + 1)
        self.parents = [i for i in range(n + 1)]
        self.amount = [1] * (n + 1)
        self.row = row
        self.col = col

    def get_parent(self, i):
        if self.parents[i] == i:
            return i

        parent = self.get_parent(self.parents[i])
        self.parents[i] = parent
        return parent

    def join(self, i, j) -> bool:

        parent_i = self.get_parent(i)
        parent_j = self.get_parent(j)

        if parent_i == parent_j: return self.top_flag[parent_i] and self.bottom_flag[parent_i]


        top_edge = (parent_i <= self.col or parent_j <= self.col)
        bottom_edge = (
                (self.row * self.col) - self.col < parent_i <= self.row * self.col
                or (self.row * self.col) - self.col < parent_j <= self.row * self.col
        )

        top_accessible = (self.top_flag[parent_i] or self.top_flag[parent_j] or top_edge)
        bottom_accessible = (self.bottom_flag[parent_i] or self.bottom_flag[parent_j] or bottom_edge)

        if self.amount[parent_i] > self.amount[parent_j]:
            self.parents[parent_j] = parent_i
            self.top_flag[parent_i] = top_accessible
            self.bottom_flag[parent_i] = bottom_accessible
            self.amount[parent_i] = self.amount[parent_i] + self.amount[parent_j]
            return self.top_flag[parent_i] and self.bottom_flag[parent_i]

        self.parents[parent_i] = parent_j
        self.top_flag[parent_j] = top_accessible
        self.bottom_flag[parent_j] = bottom_accessible
        self.amount[parent_j] = self.amount[parent_j] + self.amount[parent_i]
        return self.top_flag[parent_j] and self.bottom_flag[parent_j]

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        land_cells = set()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dsu = DSU(row * col, row, col)

        for cell_i in range(len(cells) - 1, -1, -1):
            c_row, c_col = cells[cell_i]

            for m_row, m_col in dirs:
                n_row, n_col = c_row + m_row, c_col + m_col

                if 1 <= n_row <= row and 1 <= n_col <= col and (n_row, n_col) in land_cells:
                    is_path = dsu.join((c_row - 1) * col + c_col, (n_row - 1) * col + n_col)
                    if is_path: return cell_i

            land_cells.add((c_row, c_col))

        return -1

if __name__ == "__main__":
    sln = Solution()
    print(sln.latestDayToCross(3,3,[[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]))
