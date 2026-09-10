from typing import List

# n -> len(nums)
# TC -> O(n)
# SC -> O(1)

# Approach
# Start from the i = 0 and check which idx (j) in the range(i, i + nums[i]) can bring you the furthest in the array
# (in other words we are trying to find the maximum j + nums[j]). Once found, set the l pointer to be equal to j and increment
# the min_jumps variable. Repeat this process while l < len(nums) - 1.

class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps = 0
        l = 0
        while l < len(nums) - 1:
            next_l = l + 1
            for r in range(l + 1, l + nums[l] + 1):
                if r >= len(nums) - 1: return min_jumps + 1

                if r + nums[r] >= nums[next_l] + next_l:
                    next_l = r

            min_jumps += 1
            l = next_l

        return min_jumps

if __name__ == "__main__":
    sln = Solution()
    print(sln.jump([2,1,3,1,1,2,1,5,1,1]))