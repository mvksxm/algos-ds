import heapq


# Approach:
# Maintain 3 heaps: max nums_heap (contains numbers), max median_heap (last 1 or 2 elements are medians) and min later_heap
# (contains elements that should be added to the median heap, when len(median_heap) < len(nums_heap) // 2 + 1).
# When appending a new num we need to check, if it's bigger than the current median or not -> if it is we are inputting
# it to the later_heap, so that we were able to add it later, when needed. Otherwise, in case if num <= median_heap[0]
# (less than current median) -> we are popping the biggest element from the median_queue and appending num. Popped element
# is added to the later_heap. Then we have a second check. In case if len(median_heap) < len(nums_heap) // 2 + 1, it
# means that we do not have enough values in our median_heap to calculate it, so we are popping one element from later_heap
# and inputting it to the median_heap.

# TC:
# addNum() -> O(log(n))
# findMedian() -> O(1)

# SC -> O(n)

class MedianFinder:

    def __init__(self):

        # Max Heaps
        self.nums_heap = []
        self.median_heap = []

        # Min Heap
        self.later_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.nums_heap, num)

        if not self.median_heap:
            heapq.heappush_max(self.median_heap, num)
            return

        if num <= self.median_heap[0]:
            top_median = heapq.heappop_max(self.median_heap)
            heapq.heappush_max(self.median_heap, num)
            heapq.heappush(self.later_heap, top_median)
        else:
            heapq.heappush(self.later_heap, num)

        if len(self.median_heap) != len(self.nums_heap) // 2 + 1:
            top_later = heapq.heappop(self.later_heap)
            heapq.heappush_max(self.median_heap, top_later)


    def findMedian(self) -> float:
        if len(self.nums_heap) % 2 == 0:
            f_val = self.median_heap[0]
            s_val = self.median_heap[1]
            t_val = self.median_heap[2] if len(self.median_heap) >= 3 else float('-inf')
            median = max((f_val + t_val), (f_val + s_val)) / 2
            return median

        return self.median_heap[0]