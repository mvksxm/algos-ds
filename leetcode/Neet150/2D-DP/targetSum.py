from typing import List

# n = len(nums); S = sum(nums)
# TC -> O(n * S)
# SC -> O(n * S)

# Approach
# Check every negative and positive possibilities starting from the beginning. Maintain a DP state of (idx, curr_sum).
# In case, if curr_sum == target and i == len(nums) - 1 -> it means we've reached the target, so we can return 1. Otherwise
# in case, if we've reached i == len(nums) - 1, but curr_sum != target, we are returning 0, since combination is invalid.
# On every dfs() function return populate the cache -> dp with the (idx, curr_sum): amount_possibilities, in order to no
# perform repetitive work during the subsequent calls. 'amount_possibilities' in turn is calculated by taking the amount
# of possibilities if next element is negative and adding it with the amount of possibilities if next element is positive.

class Solution:

    # Recursive DP with caching.
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(idx, curr_sum):
            if idx == len(nums) - 1 and curr_sum == target:
                return 1

            if idx == len(nums) - 1:
                return 0

            if (idx, curr_sum) in dp:
                return dp[(idx, curr_sum)]

            sub = dfs(idx + 1, curr_sum - nums[idx + 1])
            add = dfs(idx + 1, curr_sum + nums[idx + 1])
            dp[(idx, curr_sum)] = sub + add
            return dp[(idx, curr_sum)]

        return dfs(0, nums[0]) + dfs(0, -nums[0])

if __name__ == "__main__":
    sln = Solution()
    print(sln.findTargetSumWays([3,3,3,3,3], 3))