from typing import List

# TC -> O(n)
# SC -> O(1)

# Approach
# Maintain two variables: curr_sum (current sum during iteration) and mx (max sum found so far). In case, if during
# iteration we encounter an integer - num, which is bigger than curr_sum + num, we are updating the curr_sum to be
# equal to num. Otherwise, we are adding num to the curr_sum. After each iteration mx = max(mx, curr_sum) is performed.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = float('-inf')

        curr_sum = float('-inf')
        for num in nums:
            if curr_sum + num < num:
                curr_sum = num
            else:
                curr_sum += num

            mx = max(mx, curr_sum)

        return mx