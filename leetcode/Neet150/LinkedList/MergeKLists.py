from typing import Optional, List
import heapq

# Approach
# Use min heap for adding first values of the sorted lists. Then, pop first value from heap, append it to the res list
# and add the next pointer of the popped value back to the min heap.

# n -> len(longest linked list in the input array)
# k -> amount of linked lists
# TC -> O(n * k * log k) = O(n * k)
# SC -> O(log k)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        res_head = res_tail = None
        counter = 0

        for node in lists:
            if node:
                heapq.heappush(min_heap,(node.val, counter, node))
                counter += 1

        while min_heap:

            # Heap
            top_node = heapq.heappop(min_heap)
            if res_tail:
                res_tail.next = top_node[2]
            else:
                res_head = top_node[2]
            res_tail = top_node[2]

            next_node = top_node[2].next
            if next_node:
                heapq.heappush(min_heap,(next_node.val, counter, next_node))

            counter += 1

        return res_head