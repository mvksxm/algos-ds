import heapq
from typing import List


# Time Complexity:  O(n * log k)
# Space Complexity: O(k)

# Approach
# Build Min Heap from the first k elements of the array nums. Then, perform an iteration on the rest of the elements.
# In case, if element encountered is bigger than the top of value of the K Min Heap, pop the top value and append the
# element. In the end of the iteration Heap is supposed to contain top k elements sorted in ascending order. It means
# that the top of value of the Min Heap is the result that should be returned.

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for i in range(k, len(nums)):
            if min_heap[0] < nums[i]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums[i])

        return heapq.heappop(min_heap)
