from typing import List
from tester import Tester

# Approach: Dynamic Programming. Keep track of the local_min and local_max on each cycle of the for loop iteration.
# If element is negative -> update the local_max with max(nums[i], nums[i] * prev_min) and local_min with ->
# min(nums[i], prev_max * nums[i]). If element is positive - other way around. local_max = max(nums[i], nums[i] * prev_max);
# local_min = min(nums[i], nums[i] * prev_min). (Could be simplified a bit). 0 handling logic -> 0 can be only max if
# all other elements in the array are negative. So, treat 0s like 1s during the normal iteration of the for loop and
# then on return call -> max(global_max, max(nums)). It will make sure that in case if 0 is the biggest val in the array
# -> it will be returned.
# TC -> O(n)
# SC -> O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        global_max = float('-inf')
        local_min = local_max = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                local_max = 1
                local_min = 1
                continue

            max_copy = local_max
            min_copy = local_min

            if nums[i] < 0:
                local_max = max(min_copy * nums[i], nums[i])
                local_min = min(max_copy * nums[i], nums[i])

            if nums[i] > 0:
                local_max = max(max_copy * nums[i], nums[i])
                local_min = min(min_copy * nums[i], nums[i])

            global_max = max(global_max, local_max)


        return max(max(nums), global_max)

if __name__ == "__main__":
    sln = Solution()
    tst = Tester()
    tst.array_test(
 [
            [[[2, 3, -2, 4]], 6],
            [[[-2, 3, -4]], 24],
            [[[-2, 3, -4, -5]], 60],
            [[[-2, -3, 7, -2, -2]], 168],
            [[[6, -3, -10, 0, 2]], 180],
            [[[-1, -3, -10, 0, 60]], 60],
            [[[-2, 0, -1]], 0],
            [[[0, -2, -3, 0, -4]], 6],
        ],
        sln.maxProduct
    )