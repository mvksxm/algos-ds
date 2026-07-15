from typing import List

# Time Complexity: O(n), where n is the sum of amounts of unique steps that can be made at each level of a tree.
# Space Complexity:
# Would need to clean up the solution a bit.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = {}

        def dfs(idx: int):

            if idx > len(cost) - 1:
                return 0

            if idx == len(cost) - 1:
                return cost[idx]

            if idx + 1 in dp:
                left_min_cost = dp[idx + 1]
            else:
                left_min_cost = dfs(idx + 1)
                dp[idx + 1] = left_min_cost

            if idx + 2 in dp:
                right_min_cost = dp[idx + 2]
            else:
                right_min_cost = dfs(idx + 2)
                dp[idx + 2] = right_min_cost

            if idx == -1:
                return min(left_min_cost, right_min_cost)

            return min(cost[idx] + left_min_cost, cost[idx] + right_min_cost)

        return dfs(-1)