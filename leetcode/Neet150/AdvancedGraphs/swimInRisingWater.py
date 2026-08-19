from typing import List

import heapq

# TC -> O(n^2 * log(n))
# SC -> O(n^2)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        k = grid[0][0]
        min_heap = [(grid[0][0], (0, 0))]
        visited_set = {(0, 0)}

        while min_heap:
            dist, coordinates = heapq.heappop(min_heap)

            if dist > k: k = dist

            if coordinates == (len(grid) - 1, len(grid) - 1):
                break

            for dr in dirs:
                row, col = coordinates[0] + dr[0], coordinates[1] + dr[1]
                if 0 <= row < len(grid) and 0 <= col < len(grid) and (row, col) not in visited_set:
                    heapq.heappush(min_heap, (grid[row][col], (row, col)))
                    visited_set.add((row, col))

        return k