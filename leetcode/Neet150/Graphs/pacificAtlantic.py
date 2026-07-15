from typing import List
from collections import deque

# Not Optimal Approach
# Time Complexity: O((m*n)^2)
# Space Complexity: O(m*n)

# Optimal Approach

class Solution:
    def pacificAtlanticNotOptimal(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights[0]:
            return []

        # Directions
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # Coordinates Sets
        pacific_set = {(len(heights) - 1,0),(0, len(heights[0]) - 1)}
        atlantic_set = {(len(heights) - 1,0),(0, len(heights[0]) - 1)}
        result_array = []


        def dfs(row, col, visited_set) -> [bool, bool]:

            pacific_conn  = False
            atlantic_conn = False
            visited_set.add((row, col))

            # Base Cases
            if (row, col) in pacific_set and (row, col) in atlantic_set:
                return True, True
            elif (row, col) in pacific_set:
                pacific_conn = True
                atlantic_conn = False
            elif (row, col) in atlantic_set:
                pacific_conn = False
                atlantic_conn = True


            if row == 0 or col == 0:
                pacific_conn = True

            if row == len(heights) - 1 or col == len(heights[0]) - 1:
                atlantic_conn = True


            for direction in directions:

                child_row, child_col = row + direction[0], col + direction[1]

                if (
                        0 <= child_row <= len(heights) - 1
                        and 0 <= child_col <= len(heights[0]) - 1
                        and heights[row][col] >= heights[child_row][child_col]
                        and (child_row, child_col) not in visited_set
                ):

                    child_pacific, child_atlantic = dfs(child_row, child_col, visited_set)

                    if child_pacific:
                        pacific_conn = True

                    if child_atlantic:
                        atlantic_conn = True

                    if pacific_conn and atlantic_conn:
                        pacific_set.add((row, col))
                        atlantic_set.add((row, col))
                        return True, True

            if pacific_conn:
                pacific_set.add((row, col))

            if atlantic_conn:
                atlantic_set.add((row, col))

            visited_set.remove((row, col))
            return pacific_conn, atlantic_conn

        for row in range(len(heights)):
            for col in range(len(heights[0])):
                visited_set = set()
                if all(dfs(row, col, visited_set)):
                    result_array.append([row, col])

        return result_array

    def pacificAtlanticOptimal(self, heights: List[List[int]]) -> List[List[int]]:

        # Edge Case
        if not heights[0]:
            return []

        # Directions
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        pacific_set = set()
        atlantic_set = set()


        def bfs(water_queue, is_pacific: bool):

            while water_queue:

                water_row, water_col = water_queue.popleft()

                for direction in directions:
                    child_row, child_col = water_row + direction[0], water_col + direction[1]

                    if (
                            0 <= child_row <= len(heights) - 1
                            and 0 <= child_col <= len(heights[0]) - 1
                            and heights[child_row][child_col] >= heights[water_row][water_col]
                            # and ((is_pacific and (child_row, col) not in pacific_set) or (not is_pacific and (child_row, col) not in atlantic_set))
                    ):
                        if is_pacific and (child_row, child_col) not in pacific_set:
                            pacific_set.add((child_row, child_col))
                            water_queue.append((child_row, child_col))

                        if not is_pacific and (child_row, child_col) not in atlantic_set:
                            atlantic_set.add((child_row, child_col))
                            water_queue.append((child_row, child_col))


        pacific_queue = deque()
        for row in range(len(heights)):
            for col in range(len(heights[0])):

                if row > 0:
                    pacific_queue.append((row, 0))
                    pacific_set.add((row, 0))
                    break

                pacific_queue.append((row, col))
                pacific_set.add((row, col))

        bfs(pacific_queue, True)


        atlantic_queue = deque()
        for row in range(len(heights)):
            for col in range(len(heights[0])):

                if row < len(heights) - 1:
                    atlantic_queue.append((row, len(heights[0]) - 1))
                    atlantic_set.add((row, len(heights[0]) - 1))
                    break

                atlantic_queue.append((row, col))
                atlantic_set.add((row, col))

        bfs(atlantic_queue, False)

        return [[point[0], point[1]] for point in pacific_set if point in atlantic_set]

if __name__ == "__main__":
    sln = Solution()
    print(sln.pacificAtlanticOptimal(heights=[[1,1,1],[1,1,1]]))