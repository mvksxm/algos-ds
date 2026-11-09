import heapq

# n -> len(trips)
# TC -> O(n * log(n))
# SC -> O(n)

class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        min_heap = []

        trips.sort(key = lambda x: x[1])

        curr_amount = 0

        for tr in trips:
            heapq.heappush(min_heap, (tr[2], tr[0]))

            while min_heap and min_heap[0][0] <= tr[1]:
                _, left_amount = heapq.heappop(min_heap)
                curr_amount -= left_amount

            curr_amount += tr[0]

            if curr_amount > capacity: return False

        return True


