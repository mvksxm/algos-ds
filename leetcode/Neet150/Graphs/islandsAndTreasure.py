import collections
from typing import List

# Time Complexity: O(mxn); where m -> amount of rows; n -> amount of columns
# Space Complexity: O(mxn)

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        queue = collections.deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))


        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while queue:
            root_row, root_col, root_distance = queue.popleft()

            for dir in directions:
                child_row = root_row + dir[0]
                child_col = root_col + dir[1]

                if (
                        0 <= child_row <= len(grid) - 1
                        and 0 <= child_col <= len(grid[0]) - 1
                        and grid[child_row][child_col] != -1
                        and grid[child_row][child_col] > root_distance + 1
                ):
                    grid[child_row][child_col] = root_distance + 1
                    queue.append((child_row, child_col, root_distance + 1))