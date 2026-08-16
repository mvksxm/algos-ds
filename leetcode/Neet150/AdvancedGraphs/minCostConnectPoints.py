from typing import List
import heapq

# Approach: use Prim's algorithm with min heap to calculate min distances. Pop the first dot from heap and calculate
# distances to other dots and place them in heap as well. Afterward, pop the top dot from the heap and perform the same
# operation -> calculate distances to other dots and place them to the heap. This operation should be performed until
# heap is empty and all dots were visited.

# N -> len(points)
# TC -> O(N^2 * log(N))
# SC -> O(N^2)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_heap = [(0, (points[0][0], points[0][1]))]
        visited_set = set()
        min_distance = 0


        while min_heap:
            top_item = heapq.heappop(min_heap)
            dist, point = top_item
            if point in visited_set: continue
            visited_set.add(point)
            min_distance += dist

            for i in range(len(points)):
                c_point = (points[i][0], points[i][1])
                if c_point not in visited_set:
                    c_dist = abs(point[0] - c_point[0]) + abs(point[1] - c_point[1])
                    heapq.heappush(min_heap, (c_dist, c_point))

        return min_distance

if __name__ == "__main__":
    sln = Solution()
    points=[[0,0],[2,2],[3,3],[2,4],[4,2]]
    print(sln.minCostConnectPoints(points))