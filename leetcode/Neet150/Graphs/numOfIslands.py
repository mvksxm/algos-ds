from collections import deque


# Space Complexity: O(n)
# Time Complexity: O(n) + O(n) = O(n)


class Solution:

    def numIslands(self, grid: list) -> int:

        if not grid or len(grid) == 1 and not grid[0]:
            return 0

        land_queue = deque()
        visited_set = set()
        island_count = 0

        def _validate_coordinates(child_coordinates) -> bool:

            r_idx, c_idx = child_coordinates

            if r_idx < 0 or r_idx > len(grid) - 1:
                return False

            if c_idx < 0 or c_idx > len(grid[0]) - 1:
                return False

            child_value = grid[r_idx][c_idx]
            if child_coordinates in visited_set or child_value == "0":
                return False

            return True

        def _bfs(land_coordinates: tuple, island_count: int) -> int:
            land_queue.append(land_coordinates)
            visited_set.add(land_coordinates)
            while len(land_queue) > 0:
                parent_land = land_queue.popleft()
                parent_row, parent_col =  parent_land

                # Child extraction
                top_child = (parent_row - 1, parent_col)
                if _validate_coordinates(top_child):
                    land_queue.append(top_child)
                    visited_set.add(top_child)

                right_child = (parent_row, parent_col + 1)
                if _validate_coordinates(right_child):
                    land_queue.append(right_child)
                    visited_set.add(right_child)

                bottom_child = (parent_row + 1, parent_col)
                if _validate_coordinates(bottom_child):
                    land_queue.append(bottom_child)
                    visited_set.add(bottom_child)

                left_child = (parent_row, parent_col - 1)
                if _validate_coordinates(left_child):
                    land_queue.append(left_child)
                    visited_set.add(left_child)

            island_count += 1
            return island_count

        for r_idx in range(len(grid)):
            for c_idx in range(len(grid[0])):

                point = grid[r_idx][c_idx]
                point_coordinates = (r_idx, c_idx)

                if point == "1" and point_coordinates not in visited_set:
                    island_count = _bfs(point_coordinates, island_count)

        return island_count

if __name__ == "__main__":
    test_cases = [
        [
            [
                ["0","1","1","1","0"],
                ["0","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ],
            1
        ],
        [
            [
                ["1","1","0","0","1"],
                ["1","1","0","0","1"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ],
            4
        ]
    ]

    sln = Solution()
    for test in test_cases:
        assert sln.numIslands(test[0]) == test[1]