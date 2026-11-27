import heapq

# n - amount of projects
# TC -> O(n * log(n))
# SC -> O(n)

# Approach
# 1) we place all the projects to the min heap sorted by the capital needed in asc order.
# 2) we need to find the projects that we can do currently with our current amount.
# 3) we place all the projects that we can do currently in a max heap sorted by profit we can get.
#   Once we found the project that can give max profit -> we are picking the project, updating the money we have currently.
#   Performing the same steps one more time (1-3)



class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        capital_heap = []
        profit_heap = []

        for i in range(len(profits)):
            heapq.heappush(capital_heap, (capital[i], profits[i]))


        while (capital_heap or profit_heap) and k > 0:

            while capital_heap:
                if capital_heap[0][0] > w: break
                _, p_profit = heapq.heappop(capital_heap)
                heapq.heappush_max(profit_heap, p_profit)

            if not profit_heap: break
            max_profit = heapq.heappop_max(profit_heap)
            k -= 1
            w += max_profit

        return w