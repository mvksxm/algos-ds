from typing import List
from tester import Tester


# TC -> O(n)
# SC -> O(n)

class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3: return max(nums)
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))



    def helper(self, nums: list) ->  int:

        max_money = -1
        track_array = [-1] * len(nums)

        for i in range(len(nums)):

            prev_i = i - 2
            prev_j = i - 3

            if prev_i < 0:
                track_array[i] = nums[i]
                max_money = max(track_array[i], max_money)
                continue

            if prev_i == 0:
                track_array[i] = nums[i] + track_array[prev_i]
                max_money = max(max_money, track_array[i])
                continue

            local_sum = max(track_array[prev_i],track_array[prev_j]) + nums[i]

            max_money = max(local_sum, max_money)
            track_array[i] = local_sum

        return max_money




if __name__ == "__main__":
    sln = Solution()
    tst = Tester()

    test_list = [
        # Official examples
        [[[2, 3, 2]], 3],
        [[[1, 2, 3, 1]], 4],
        [[[1, 2, 3]], 3],

        # Empty / single house
        [[[5]], 5],
        [[[0]], 0],

        # Two houses
        [[[2, 3]], 3],
        [[[5, 5]], 5],
        [[[1, 10]], 10],

        # Three houses
        [[[2, 1, 2]], 2],
        [[[10, 1, 1]], 10],
        [[[1, 10, 1]], 10],
        [[[1, 1, 10]], 10],

        # Circle matters
        [[[1, 2, 1, 1]], 3],
        [[[1, 1, 2, 1]], 3],
        [[[100, 1, 1, 100]], 101],
        [[[10, 1, 10, 1, 10]], 20],

        # Increasing values
        [[[1, 2, 3, 4, 5]], 8],
        [[[2, 4, 6, 8, 10]], 16],

        # Decreasing values
        [[[5, 4, 3, 2, 1]], 8],
        [[[10, 8, 6, 4, 2]], 16],

        # All equal
        [[[1, 1, 1, 1]], 2],
        [[[5, 5, 5, 5]], 10],
        [[[7, 7, 7, 7, 7]], 14],

        # Alternating values
        [[[10, 1, 10, 1]], 20],
        [[[1, 10, 1, 10]], 20],
        [[[9, 1, 9, 1, 9]], 18],

        # Zeros
        [[[0, 0, 0]], 0],
        [[[0, 5, 0, 5]], 10],
        [[[5, 0, 5]], 5],

        # Larger examples
        [[[2, 7, 9, 3, 1]], 11],
        [[[6, 6, 4, 8, 4, 3, 3, 10]], 27],
        [[[200, 3, 140, 20, 10]], 340],

        # Tricky edge cases
        [[[4, 1, 2, 7, 5, 3, 1]], 14],
        [[[8, 2, 8, 9, 2]], 17],
        [[[1, 3, 1, 3, 100]], 103],
        [[[2,1,4,7,5,15,10,10]], 33],
    ]

    tst.array_test(test_list, sln.rob)