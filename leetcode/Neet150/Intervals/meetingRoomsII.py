import heapq
from typing import List


# TC -> O(n * log(n))
# SC -> O(n)

# Approach: sort intervals and iterate through them. If there is an overlap add current interval's end time to the min
# heap and increment rooms count. Otherwise, if there is no overlap -> pop top element, insert current interval's end
# and do not increment rooms count.

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: (x.start, x.end))
        heap = []
        rooms = 0

        for interval in intervals:

            if not heap:
                rooms = 1
                heapq.heappush(heap, interval.end)
                continue

            top_elem = heap[0]
            if top_elem <= interval.start:
                heapq.heappop(heap)
                heapq.heappush(heap, interval.end)
            else:
                heapq.heappush(heap, interval.end)
                rooms += 1

        return rooms