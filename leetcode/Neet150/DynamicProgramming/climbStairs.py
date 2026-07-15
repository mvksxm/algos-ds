
# Recursive Approach
# Time Complexity: O(n), where n is the sum of the amount of unique steps that can be performed on each level of a tree.
# Space Complexity: O(m) -> recursion stack, where m is the amount of stairs; + O(n) -> length of the dp map. Final - O(n)

class Solution:
    def climbStairs(self, n: int) -> int:

        dp = {}

        def dfs(local_sum: int) -> int:

            if local_sum == n:
                return 1

            if local_sum > n:
                return 0

            if local_sum in dp:
                return dp[local_sum]

            sum_of_steps = dfs(local_sum + 1) + dfs(local_sum + 2)
            dp[local_sum] = sum_of_steps
            return sum_of_steps

        return dfs(0)
