
# n -> len(nums)
# TC -> O(n)
# SC -> O(1)

# Approach
# Use bit manipulation. Specifically, perform 'XOR' operation on current 'target_num' and current number in the loop.
# Once performed, update the target_num with the result. After the loop ends, it's guaranteed that 'target_num' will
# be equal to the num that appears only once in the 'nums' array.


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        target_num = nums[0]

        for i in range(1, len(nums)):
            target_num = nums[i] ^ target_num
            i += 1

        return target_num