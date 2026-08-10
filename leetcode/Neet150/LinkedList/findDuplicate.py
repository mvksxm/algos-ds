from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s_p = 0
        q_p = 0

        while True:
            s_p = nums[s_p]
            q_p = nums[nums[q_p]]

            if s_p == q_p:
                break

        s_p2 = 0
        while True:
            s_p = nums[s_p]
            s_p2 = nums[s_p2]

            if nums[s_p] == nums[s_p2]:
                break

        return nums[s_p]



if __name__ == "__main__":
    nums=[1,2,3,2,2]
    sln = Solution()
    sln.findDuplicate(nums)