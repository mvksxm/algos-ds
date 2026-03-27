import math
import heapq

# Time Complexity (Heap) - O(n * log k) + O(k * log k) = O(n * log k)
# Space Complexity (Heap) - O(k) + O(k) = O(k)

# Time Complexity (Merge Sort) - O(n * log n)
# Space Complexity (Merge Sort) - O(n)

# Approach (Merge Sort)
# Implement Merge Sort and sort the points in the ascending order by the result of the formula -
# - math.sqrt(point1**2 + point2**2). In the end, pick first k coordinates from the result array.

# Approach (Heap)
# Build a Max Heap of the size k from the first k unsorted points. Heap should be built based on the result of the
# math.sqrt(point1**2 + point2**2) formula. Then, iterate through the rest of the points. In case, if the distance of
# the point encountered is smaller than the top value of the Max Heap - pop the max from the heap and input the point.
# After the iteration, pop all the values from the Max Heap and fill the result array starting from the end.


class Solution:
    def kClosest(self, points: list, k: int) -> list:


        # Sorting Approach (Raw) (Merge Sort)
        # sorted_points = Solution.merge_sort(points)
        # return sorted_points[:k]

        # Sorting Approach (Simple)
        # sorted_points = sorted(points, key=lambda x: math.sqrt(x[0]**2+x[1]**2))
        # return sorted_points[:k]

        # Heap Approach (Space Optimized)
        points_max_heap = []
        for i in range(k):
            points_max_heap.append((Solution.calculate_distance(points[i]), points[i]))

        heapq.heapify_max(points_max_heap)

        for i in range(k, len(points)):
            dist = Solution.calculate_distance(points[i])
            max_heap_elem = points_max_heap[0]

            if dist < max_heap_elem[0]:
                heapq.heappop_max(points_max_heap)
                heapq.heappush_max(points_max_heap, (dist, points[i]))

        res = [None] *  k
        for i in range(k-1, -1, -1):
            res[i] = heapq.heappop_max(points_max_heap)[1]

        return res


    @staticmethod
    def merge_sort(arr: list):

        if len(arr) <= 1:
            return arr

        mid_idx = len(arr) // 2

        left_part = arr[:mid_idx]
        right_part = arr[mid_idx:]

        return Solution.merge_arrays(Solution.merge_sort(left_part), Solution.merge_sort(right_part))

    @staticmethod
    def merge_arrays(l_arr, r_arr) -> list:

        if not l_arr: return r_arr
        if not r_arr: return l_arr

        merged_arr = []

        l_arr_p = 0
        r_arr_p = 0

        while l_arr_p < len(l_arr) and r_arr_p < len(r_arr):

            l_arr_distance = Solution.calculate_distance(l_arr[l_arr_p])
            r_arr_distance = Solution.calculate_distance(r_arr[r_arr_p])

            if l_arr_distance < r_arr_distance:
                merged_arr.append(l_arr[l_arr_p])
                l_arr_p += 1
            else:
                merged_arr.append(r_arr[r_arr_p])
                r_arr_p += 1

        if l_arr_p < len(l_arr):
            merged_arr += l_arr[l_arr_p:]

        if r_arr_p < len(r_arr):
            merged_arr += r_arr[r_arr_p: ]

        return merged_arr


    @staticmethod
    def calculate_distance(point: list) -> float:
        return math.sqrt(point[0]**2 + point[1]**2)


if __name__ == "__main__":
    points = [[0,2],[2,2]]
    k = 1
    sln = Solution()
    print(sln.kClosest(points, k))