from collections import defaultdict
from typing import List

# Canonical Solution
# n -> len(freq_map) (number of unique points)
# TC -> O(n)
# SC -> O(n)
# Approach
# Key to this problem is to find a point that is located diagonally from the provided point. In order to do that, we
# need to find a point, which has coordinates (searched_px, searched_py), where
# abs(provided_px - searched_px) == abs(provided_py - searched_py). This formula means that the x distance and y distance
# from the provided point to the searched point should be equal. It makes sense, because in a usual square, points,
# which are located on a diagonal have an equal distances y and x between them.
# Once diagonal point was found, we are searching for a point which is located on the same y coordinate as the provided
# point and on x diagonal as the searched point. Also, we are searching for a point which is located on the same x
# coordinate as the provided point and on the same y coordinate as the searched point. Once all points were found,
# their frequencies in freq_map are being multiplied between each other.

# Canonical
class DetectSquares:

    def __init__(self):
        self.freq_map = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.freq_map[(point[0], point[1])]  += 1

    def count(self, point: List[int]) -> int:
        p1_x, p1_y = point
        sm = 0

        for coordinates in list(self.freq_map.keys()):
            p_x, p_y = coordinates
            if abs(p1_x - p_x) == abs(p1_y - p_y) and (p1_x != p_x and  p1_y != p_y):
                possibilities = self.freq_map[(p_x, p_y)] * self.freq_map[(p_x, p1_y)] * self.freq_map[(p1_x, p_y)]
                sm += possibilities

        return sm


# Brute Force
class DetectSquaresBrute:

    def __init__(self):
        self.x_map = defaultdict(list)
        self.y_map = defaultdict(list)

    def add(self, point: List[int]) -> None:

        self.x_map[point[0]].append(point[1])
        self.y_map[point[1]].append(point[0])

    def count(self, point: List[int]) -> int:
        visited_map = {} #  point: count

        def dfs(cnt, coordinates , distance):

            if coordinates in visited_map:
                return visited_map[coordinates]

            sm = 0
            x_axis, y_axis = coordinates

            # Initial dot
            if cnt == 0:
                # X dots
                for x in self.y_map[y_axis]:
                    if x == x_axis: continue
                    sm += dfs(cnt + 1, (x, y_axis), abs(x_axis - x))

            if cnt == 1:
                # Y dots
                for y in self.x_map[x_axis]:
                    if y == y_axis: continue
                    if abs(y_axis - y) == distance:
                        sm += dfs(cnt + 1, (x_axis, y), distance)

            if cnt == 2:
                # X dots
                for x in self.y_map[y_axis]:
                    if x == point[0]:
                        sm += dfs(cnt + 1, (x, y_axis), distance)

            if cnt == 3:
                # Y dots
                return 1

            visited_map[coordinates] = sm
            return sm

        return dfs(0, (point[0], point[1]), 0)

if __name__ == "__main__":
    cs = DetectSquares()
    cs.add([3,10])
    cs.add([11, 2])
    cs.add([3, 2])
    cs.add([11, 2])
    print(cs.count([11, 10]))