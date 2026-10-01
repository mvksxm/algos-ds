from typing import List

# TC -> O(n)
# SC -> O(n)
# Approach:
# Key here is the nn_i, which is an initial index of the non_negative array from which we should start a substitution of
# the non-negative vals in the nums array. We calculate it by performing a k % len(non_negative), it allows us to understand
# which num from the non_negative array should be in the place of the current one after rotation.

class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:

        non_negative = [n for n in nums if n >= 0]

        if not non_negative or k == 0 or len(non_negative) == k:
            return nums

        nn_i = k % len(non_negative)

        for i in range(len(nums)):
            if nums[i] >= 0:
                nums[i] = non_negative[nn_i]
                nn_i = nn_i + 1 if nn_i < len(non_negative) - 1 else 0

        return nums

if __name__ == "__main__":
    sln = Solution()
    print(sln.rotateElements([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], 1))
