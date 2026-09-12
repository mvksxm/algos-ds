from typing import List
import heapq


# n -> len(intervals)
# m -> len(queries)
# TC -> O(n * log(n) + m * log(m))
# SC -> O(m + n)

# Approach (Min Heap)
# Sort queries and intervals. Iterate through the sorted list of queries and for each query -> place an interval from
# the sorted list of intervals whose start value (0 idx) is smaller than the query into the min heap. At the same time
# increment pointer 'i' on each push to the heap, so that next query could start from the interval that was not visited yet.
# Once all suitable intervals were pushed -> pop the unsuitable ones from the heap (ones whose end time is smaller than
# the query). After all unsuitable ones were popped -> the one that left on top of the heap has the min len for the query.
# If there are no elements left in a heap -> query can't be placed in any of the intervals, so assign it a value of -1.

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        q_map = {}
        s_queries = sorted(queries)
        intervals.sort()
        min_heap = []

        i = 0
        for q in s_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                l = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(min_heap,(l, intervals[i][1]))
                i += 1

            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            q_map[q] = min_heap[0][0] if min_heap else -1

        return [q_map[q] for q in queries]

if __name__ == "__main__":
    sln = Solution()
    intervals = [[1,3],[2,3],[3,7],[6,6]]
    print(sorted(intervals, key = lambda x: (x[1], x[0])))
