
# TC -> O(log(n))
# SC -> O(1)

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l_p = 0
        r_p = len(nums) - 1
        nums_len = len(nums)

        while l_p <= r_p:
            mid = l_p + (r_p - l_p) // 2

            left_num = float('-inf') if mid - 1 < 0 else nums[mid - 1]
            right_num = float('-inf') if mid + 1 >= nums_len else nums[mid + 1]

            if (left_num < nums[mid] > right_num):
                return mid

            if (left_num < nums[mid] < right_num):
                l_p = mid + 1
            else:
                r_p = mid - 1


        return -1