from typing import List

# Iterative Approach
# Time Complexity: O(n), where n is the amount of elements in the array
# Space Complexity: O(n), where n is the amount of elements in the array

# Recursive Approach
# Time Complexity: O(n), where n is the sum of unique steps on each level of a tree.

class Solution:

    # Iterative Approach
    def robIterative(self, nums: List[int]) -> int:

        max_value = 0
        max_money_array = [None] * len(nums)

        i = 0
        while i < len(nums):
            if i - 2 < 0:
                max_value = max(max_value, nums[i])
                max_money_array[i] = nums[i]
            elif i - 3 < 0:
                max_value = max(max_value, nums[i] + max_money_array[i - 2])
                max_money_array[i] = max_value
            else:
                max_value = max(max_value, nums[i] + max_money_array[i - 2],nums[i] + max_money_array[i - 3])
                max_money_array[i] = max_value

            i += 1

        return max_value

    # Recursive
    def robRecursive(self, nums: List[int]) -> int:

        dp = {}
        def dfs(idx: int) -> int:

            if idx > len(nums) - 1: return 0
            if idx == len(nums): return nums[idx]
            if idx in dp: return dp[idx]

            max_sum = max(dfs(idx + 2), dfs(idx + 3)) + nums[idx]
            dp[idx] = max_sum
            return max_sum

        return max(dfs(0), dfs(1))