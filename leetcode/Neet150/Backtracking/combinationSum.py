from typing import List

# Time Complexity:  n^(t/m), m ->  the smallest number in the array
# Space Complexity: O(t/m), where m is the smallest number in the array nums.

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(
                nums_added: list,
                nums_left: list,
                sm: int,
                res: list
        ):

            if sm > target:
                return

            if sm == target:
                res.append(nums_added)
                return

            for i in range(len(nums_left)):
                dfs(nums_added + [nums_left[i]], nums_left[i:], sm + nums_left[i], res)

        dfs([], nums, 0, res)
        return res

if __name__ == "__main__":
    sln = Solution()
    print(sln.combinationSum([2,5,6,9], 9))
# [2, 5, 6, 9 ]; t = 9
