

# TC -> O(log(n))
# SC -> O(1)

class Solution:

    def searchRange(self, nums: list[int], target: int) -> list[int]:

        min_idx = -1
        max_idx = -1

        # Binary Search for start
        l_p = 0
        r_p = len(nums) - 1

        while l_p <= r_p:
            mid_idx = l_p + (r_p - l_p) // 2
            mid_val = nums[mid_idx]

            if mid_val == target:
                min_idx = mid_idx

            if mid_val >= target:
                r_p = mid_idx - 1
            else:
                l_p = mid_idx + 1

        # Binary Search for finish
        l_p = 0
        r_p = len(nums) - 1

        while l_p <= r_p:
            mid_idx = l_p + (r_p - l_p) // 2
            mid_val = nums[mid_idx]

            if mid_val == target:
                max_idx = mid_idx

            if mid_val <= target:
                l_p = mid_idx + 1
            else:
                r_p = mid_idx - 1

        return [min_idx, max_idx]

if __name__ == "__main__":
    sln = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    print(sln.searchRange(nums, target))