from typing import List


# Approach
# Usual backtracking. For each queen position - calculate unavailable points -> send unavailable points deeper into
# the recursion stack. In case if queen can be placed -> place another queen; add more unavailable points and proceed
# further with recursion.

# TC -> O(n!)
# SC -> O(n^2)

class Solution:
    def getUnavailablePoints(
            self,
            n,
            init_coordinates,
            backtrack_coordinates,
            all_coordinates
    ):
        y = init_coordinates[0]
        x = init_coordinates[1]

        # X points
        iter_x = 0
        while iter_x < n:
            cr = (y, iter_x)
            if cr not in all_coordinates:
                backtrack_coordinates.add(cr)
                all_coordinates.add(cr)
            iter_x += 1

        # Y points
        iter_y = 0
        while iter_y < n:
            cr = (iter_y, x)
            if cr not in all_coordinates:
                backtrack_coordinates.add(cr)
                all_coordinates.add(cr)
            iter_y += 1

        # Left Diagonal
        y_init = y - x if (y - x) > 0 else 0
        x_init = x - y if (x - y) > 0 else 0
        left_point = (y_init, x_init)
        while 0 <= left_point[0] < n and 0 <= left_point[1] < n:
            if left_point not in all_coordinates:
                backtrack_coordinates.add(left_point)
                all_coordinates.add(left_point)
            left_point = (left_point[0] + 1, left_point[1] + 1)

        # Right Diagonal
        last_idx = n - 1
        y_init = y - (last_idx - x) if y - (last_idx - x) > 0 else 0
        x_init = x + y if (x + y) < last_idx else last_idx
        right_point = (y_init, x_init)
        while 0 <= right_point[0] < n and 0 <= right_point[1] < n:
            if right_point not in all_coordinates:
                backtrack_coordinates.add(right_point)
                all_coordinates.add(right_point)
            right_point = (right_point[0] + 1, right_point[1] - 1)

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def dfs(y, solution, unavailable_points):

            if y == n:
                res.append(solution.copy())
                return

            backtrack_set = set()

            # Set unavailable points
            for x in range(n):
                queen_coordinate = (y, x)
                if queen_coordinate in unavailable_points: continue
                self.getUnavailablePoints(n, queen_coordinate, backtrack_set, unavailable_points)
                solution.append(("." * x) + "Q" + ("." * (n - 1 - x)))
                dfs(y + 1, solution, unavailable_points)

                # Backtrack
                solution.pop()
                for coordinate in backtrack_set:
                    unavailable_points.remove(coordinate)
                    backtrack_set = set()

        dfs(0, [], set())
        return res

if __name__ == "__main__":
    sln = Solution()
    print(sln.solveNQueens(4))