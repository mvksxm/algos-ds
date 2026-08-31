from typing import List

from tester import Tester

# DP-based solution
# TC -> O(n^2)
# SC -> O(n)

# Binary Search solution
# TC -> O(n * log(n))
# SC -> O(n)

# Binary Search Approach
# Create an array -> 'max_sequence', which, at the beginning would contain only the first number. The main purpose of
# this array is to have a len of the max increasing subsequence up until the particular curr iteration idx
# and max_sequence[-1] is supposed to be equal to the max tip among all the increasing subsequences encountered up until
# the current iteration idx.
# During the for loop iteration, in case if encountered a num, which is <= tip, we need to place it to the 'max_sequence'
# instead of the first bigger value or the equal value. This operation is performed by using Binary Search. Otherwise,
# we should append this num to the end of the 'max_sequence'. After iteration is finished, we can assume that
# 'max_sequence' array has a length which is equal to the length of a max increasing sequence of the nums array, so
# we return len(max_sequence).


class Solution:

    # DP with memoization
    def lengthOfLISDP(self, nums: List[int]) -> int:

        dp = {}
        global_max = float("-inf")
        def dfs(i):
            nonlocal global_max
            if i in dp:
                return dp[i]

            if i >= len(nums):
                return 0

            max_count = 0
            for j in range(i + 1, len(nums)):
                if j in dp and nums[j] > nums[i]:
                    max_count = max(dp[j], max_count)
                elif nums[j] > nums[i]:
                    max_count = max(dfs(j), max_count)

            max_count += 1
            dp[i] = max_count
            global_max = max(max_count, global_max)
            return max_count

        [dfs(i) for i in range(len(nums))]
        return global_max

    def find_first_bigger(self, search_arr, num) -> int:
        l_p = 0
        r_p = len(search_arr) - 1
        max_idx = -1

        while l_p <= r_p:
            pivot = l_p + (r_p - l_p) // 2
            if search_arr[pivot] == num:
                return pivot
            if search_arr[pivot] < num:
                l_p = pivot + 1
            else:
                max_idx = pivot
                r_p = pivot - 1

        if max_idx == -1: return -1
        return max_idx

    # Binary Search approach
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_sequence = [nums[0]]

        for i in range(1, len(nums)):
            max_element = max_sequence[-1]
            if nums[i] > max_element:
                max_sequence.append(nums[i])
            else:
                bigger_idx = self.find_first_bigger(max_sequence, nums[i])
                max_sequence[bigger_idx] = nums[i]

        return len(max_sequence)

if __name__ == "__main__":
    sln = Solution()
    tst = Tester()
    tst.array_test([
            [[[1]], 1],
            [[[1, 2]], 2],
            [[[2, 1]], 1],
            [[[1, 2, 3, 4, 5]], 5],
            [[[5, 4, 3, 2, 1]], 1],

            [[[2, 2, 2, 2]], 1],
            [[[1, 2, 2, 3]], 3],
            [[[1, 1, 1, 2, 2, 3]], 3],
            [[[3, 3, 2, 2, 1, 1]], 1],

            [[[10, 9, 2, 5, 3, 7, 101, 18]], 4],
            [[[0, 1, 0, 3, 2, 3]], 4],
            [[[4, 10, 4, 3, 8, 9]], 3],
            [[[3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]], 6],
            [[[10, 22, 9, 33, 21, 50, 41, 60]], 5],
            [[[1, 3, 6, 7, 9, 4, 10, 5, 6]], 6],
            [[[2, 1, 5, 3, 6, 4, 8, 7, 9]], 5],

            [[[-1, 0, 1, 2, 3]], 5],
            [[[-5, -4, -3, -2, -1]], 5],
            [[[-1, -2, -3, 0, 1]], 3],
            [[[-10, -1, -5, 0, 3, 2, 4]], 5],
            [[[3, -2, -1, 0, 2, 1, 5]], 5],

            [[[1, 3, 2, 4, 3, 5]], 4],
            [[[2, 5, 3, 7, 11, 8, 10, 13, 6]], 6],
            [[[5, 1, 6, 2, 7, 3, 8, 4, 9]], 5],
            [[[9, 1, 8, 2, 7, 3, 6, 4, 5]], 5],
            [[[3, 4, 1, 2, 8, 5, 6, 7]], 5],

            [[[3, 10, 2, 1, 20]], 3],
            [[[10, 1, 2, 3, 4, 0, 5]], 5],
            [[[1, 100, 2, 3, 4]], 4],
            [[[4, 5, 1, 2, 3, 6]], 4],
            [[[7, 1, 2, 8, 3, 4, 5]], 5],

            [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], 10],
            [[[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]], 1],
            [[[1, 3, 5, 2, 2, 2, 4, 6, 8, 7, 9]], 6],
            [[[100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]], 1],
        ],
        sln.lengthOfLISDP
    )
