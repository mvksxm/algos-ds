import heapq

# TC -> O(m * n * log(m * n)
# SC -> O(m * n)
# Approach -> Dijkstra

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        min_heap = [(0, 0, 0)]
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited_set = set()

        while min_heap:
            weight, row, col = heapq.heappop(min_heap)
            if row == len(heights) - 1 and col == len(heights[0]) - 1:
                return weight

            if (row,  col) not in visited_set:
                for r_m, c_m in dirs:
                    r_n, c_n = row + r_m, col + c_m

                    if 0 <= r_n < len(heights) and 0 <= c_n < len(heights[0]):
                        diff = abs(heights[row][col] - heights[r_n][c_n])
                        heapq.heappush(min_heap, (max(weight, diff), r_n, c_n))


                visited_set.add((row, col))

        return -1