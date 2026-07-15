from typing import List
from collections import deque

# Not Optimal Solution (First thought)
# Time Complexity: O((m*n)^2)
# Space Complexity: O(m*n)

# Optimal Solution
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

class Solution:
    def orangesRottingNonOptimal(self, grid: List[List[int]]) -> int:


        distance_grid = []
        for _ in range(len(grid)):
            distance_grid.append([-1] * len(grid[0]))

        def _validate_coordinates(row, col, distance) -> bool:
            if row > len(grid) - 1 or row < 0:
                return False

            if col > len(grid[0]) - 1 or col < 0:
                return False

            point = grid[row][col]
            if point == 0 or point == 2:
               return False

            if distance_grid[row][col] != -1 and distance > distance_grid[row][col]:
                return False

            return True

        def _bfs(row, col):

            visited_set = set()
            queue = deque()
            queue.append((row, col, 0))
            distance_grid[row][col] = 0

            while queue:
                row, col, distance = queue.popleft()

                if (row - 1, col) not in visited_set and _validate_coordinates(row - 1, col, distance + 1):
                    queue.append((row - 1, col, distance + 1))
                    distance_grid[row - 1][col] = distance + 1
                    visited_set.add((row - 1, col))

                if (row, col + 1) not in visited_set and _validate_coordinates(row, col + 1, distance + 1):
                    queue.append((row, col + 1, distance + 1))
                    distance_grid[row][col + 1] = distance + 1
                    visited_set.add((row, col + 1))

                if (row + 1, col) not in visited_set and _validate_coordinates(row + 1, col, distance + 1):
                    queue.append((row + 1, col, distance + 1))
                    distance_grid[row + 1][col] = distance + 1
                    visited_set.add((row + 1, col))

                if (row, col - 1 ) not in visited_set and _validate_coordinates(row, col - 1 , distance + 1):
                    queue.append((row, col - 1 , distance + 1))
                    distance_grid[row][col - 1 ] = distance + 1
                    visited_set.add((row, col - 1 ))


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    _bfs(row, col)


        max_distance = 0
        for row in range(len(distance_grid)):
            for col in range(len(distance_grid[0])):
                max_distance = max(max_distance, distance_grid[row][col])
                if grid[row][col] == 1 and distance_grid[row][col] == -1:
                    return -1

        return max_distance

    def orangesRottingOptimal(self, grid: List[List[int]]) -> int:


        fruits_queue = deque()
        fresh_count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                grid_entry = grid[row][col]
                if grid_entry == 2:
                    fruits_queue.append((row, col, 0))
                if grid_entry == 1:
                    fresh_count += 1

        def _validate_coordinates(row, col) -> bool:

            if row > len(grid) - 1 or row < 0:
                return False

            if col > len(grid[0]) - 1 or col < 0:
                return False

            point = grid[row][col]
            if point == 0 or point == 2:
                return False

            return True

        max_time = 0
        while fruits_queue:
            row, col, distance = fruits_queue.popleft()

            if _validate_coordinates(row - 1, col):
                fruits_queue.append((row - 1, col, distance + 1))
                grid[row - 1][col] = 2
                fresh_count -= 1
                max_time = max(distance + 1, max_time)

            if _validate_coordinates(row, col + 1):
                fruits_queue.append((row, col + 1,distance + 1))
                grid[row][col + 1] = 2
                fresh_count -= 1
                max_time = max(distance + 1, max_time)


            if _validate_coordinates(row + 1, col):
                fruits_queue.append((row + 1, col,distance + 1))
                grid[row + 1][col] = 2
                fresh_count -= 1
                max_time = max(distance + 1, max_time)

            if _validate_coordinates(row, col - 1):
                fruits_queue.append((row, col - 1, distance + 1))
                grid[row][col - 1] = 2
                fresh_count -= 1
                max_time = max(distance + 1, max_time)

        return max_time if fresh_count == 0 else -1


if __name__ == "__main__":
    sln = Solution()
    print(sln.orangesRottingOptimal([[1,2]]))


# [
#     [2,1,0],
#     [0,1,1],
#     [0,1,2]
# ]
