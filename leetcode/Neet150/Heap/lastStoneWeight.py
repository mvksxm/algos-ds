import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) >= 2:

            top_element_1 = heapq.heappop_max(stones)
            top_element_2 = heapq.heappop_max(stones)

            if top_element_1 > top_element_2:
                heapq.heappush_max(stones, top_element_1 - top_element_2)

            if top_element_2 > top_element_1:
                heapq.heappush_max(stones, top_element_2 - top_element_1)


        return 0 if not stones else stones[0]

if __name__ == "__main__":
    sln = Solution()
    stones=[7,6,7,6,9]
    print(sln.lastStoneWeight(stones))



