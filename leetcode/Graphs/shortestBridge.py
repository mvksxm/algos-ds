from collections import deque

# n -> len(grid) and len(grid[0));
# TC -> O(n^2)
# SC -> O(n^2)

# Approach: BFS from the border of one island.

class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        borders_q = deque([])
        island_queue = deque([])

        for r in range(len(grid)):
            found = False
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    island_queue.append((r, c))
                    found = True
                    break

            if found: break

        # Searching for borders
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        visited_set = {island_queue[0]}
        while island_queue:

            top_island = island_queue.popleft()
            row, col = top_island

            for dr_row, dr_col in dirs:
                new_row = row + dr_row
                new_col = col + dr_col

                if (
                        0 <= new_row < len(grid)
                        and 0 <= new_col < len(grid[0])
                        and (new_row, new_col) not in visited_set
                ):
                    if grid[new_row][new_col] == 0:
                        borders_q.append((new_row, new_col, 1))
                    if grid[new_row][new_col] == 1:
                        island_queue.append((new_row, new_col))
                    visited_set.add((new_row, new_col))

        min_distance = float('inf')
        while borders_q:
            row, col, dist = borders_q.popleft()

            for dr_row, dr_col in dirs:
                n_row = row + dr_row
                n_col = col + dr_col
                if (
                        0 <= n_row < len(grid)
                        and 0 <= n_col < len(grid[0])
                        and (n_row, n_col) not in visited_set
                ):
                    if grid[n_row][n_col] == 0:
                        borders_q.append((n_row, n_col, dist + 1))
                    if grid[n_row][n_col] == 1:
                        min_distance = min(min_distance, dist)
                    visited_set.add((n_row, n_col))

        return min_distance

