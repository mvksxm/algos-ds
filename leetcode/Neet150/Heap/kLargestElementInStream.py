from typing import List
import heapq

# Time Complexity: add() - O(log n); initial heapify - O(n) + k * O(log n)
# Space Complexity: O(k); k - length of the maintained min heap

# Approach
# Initially min heapify the input array and remove from it (len(array) - k) top integers in order to make it of size k
# and to ensure that it contains only k largest elements. On each 'add()' operation add a 'val' to the k-largest heap
# and then right away pop the smallest element from the top of it, this operation makes sure that the in the k-largest
# heap the top value is always the k largest. In the end, return the element under the index 0 from the array that is
# backing the heap, because it represents the smallest value.

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k
        self._nums = nums
        self._k_heapify()


    def _k_heapify(self):

        if not self._nums: return

        to_pop = len(self._nums) - self._k
        heapq.heapify(self._nums)

        while to_pop > 0:
            heapq.heappop(self._nums)
            to_pop -= 1


    def add(self, val: int) -> int:
        heapq.heappush(self._nums, val)

        if len(self._nums) > self._k:
            heapq.heappop(self._nums)

        return self._nums[0]

if __name__ == "__main__":
    kth = KthLargest(3, [4, 5, 8, 2])
    print(kth.add(3))
    print(kth.add(5))
    print(kth.add(10))
    print(kth.add(9))
    print(kth.add(4))



#      4
#    /   \
#   5     8
#  / \
# 2   3

# [4, 5, 8, 2, 3]