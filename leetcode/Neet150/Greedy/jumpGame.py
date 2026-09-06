from typing import List

# TC -> O(n)
# SC -> O(1)

# Approach: maintain the smallest index of the slot in the array from which it's possible to reach the end. In the end,
# if the smallest idx is 0 -> return True.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_possible = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            dist = last_possible - i
            if nums[i] >= dist:
                last_possible = i

        return last_possible == 0

if __name__ == "__main__":
    sln = Solution()
    print(sln.canJump([1,0,1,0]))


