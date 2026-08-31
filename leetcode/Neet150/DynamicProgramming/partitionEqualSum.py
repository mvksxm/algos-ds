from typing import List

from tester import Tester

# n -> len(nums)
# t -> sum(nums) // 2

# 1) Recursion with memoization
# TC -> O(n^2 * t)
# SC -> O(n * t)

# 2) 1-D Knapsack approach
# TC -> O(n * t)
# SC -> O(t)

# 1-D Knapsack approach - create an array dp with len of sum(nums) // 2 filled with 'False' values. Each individual item
# in the array dp represents, if it's possible to get the number i (index of the array) by using values from the nums array.
# However, approach is a bit different from the Coin Change solution, due to the fact that each num can be used only
# once. So, in the outer loop we should iterate through the nums array and in the inner loop through the dp array and
# check, if it's possible to get the amount i by using current num. We can assume that it's possible to get the current
# amount i if dp[i - num] == True or dp[i] == True already. Then, after iteration is finished, we return dp[half_sum],
# which provides us info, if we were able to get half_sum with vals available in the nums array.

class Solution:
    # Recursion with memoization approach.
    def canPartitionRecursion(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0:
            return False

        half_sum = total // 2
        dp = {}

        def dfs(i, curr_sum):

            mem_key = (i, curr_sum)

            if curr_sum == half_sum:
                return True

            if curr_sum > half_sum or i >= len(nums):
                dp[mem_key] = False
                return False

            if mem_key in dp:
                return dp[mem_key]

            for j in range(i + 1, len(nums)):
                if (j, curr_sum + nums[j]) not in dp and dfs(j, curr_sum + nums[j]):
                    return True

            dp[mem_key] = False
            return False


        for i in range(len(nums)):
            if dfs(i, nums[i]):
                return True

        return False

    # 1-D DP Knapsack approach
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        half_sum = total // 2
        dp = [False] * (half_sum + 1)
        dp[0] = True

        for num in nums:
            for i in range(half_sum, -1, -1):
                if num <= i:
                    dp[i] = dp[i - num] or dp[i]

        return dp[half_sum]

if __name__ == "__main__":
    sln = Solution()
    nums = [2,2,1,1]
    sln.canPartition(nums)
    tst = Tester()
    tst.array_test(
        [
            [[[1, 5, 11, 5]], True],
            [[[1, 2, 3, 5]], False],
            [[[1, 2, 5, 6]], True],
            [[[1, 3, 4, 8]], True],
            [[[2, 3, 5, 6]], True],
            [[[3, 3, 3, 4, 5]], True],
            [[[1, 2, 3, 4, 6]], True],
            [[[1, 1, 1, 1, 1, 1, 1, 1]], True],
            [[[2, 2, 2, 2, 2, 2, 2, 2]], True],
            [[[2, 3, 7]], False],
        ],
        sln.canPartition
    )