

# TC -> O(log(n))
# SC -> O(1)

class Solution:
    def search(self, nums: list[int], target: int) -> int:

        l_p = 0
        r_p = len(nums) - 1

        while l_p <= r_p:
            mid_p = l_p + (r_p - l_p) // 2

            if nums[mid_p] == target:
                return mid_p

            if nums[l_p] <= target <= nums[r_p]:
                if nums[mid_p] < target:
                    l_p = mid_p + 1
                else:
                    r_p = mid_p - 1
            elif nums[mid_p] <= target <= nums[r_p]:
                l_p = mid_p + 1
            elif nums[l_p] <= target <= nums[mid_p]:
                r_p = mid_p - 1
            elif nums[l_p] <= nums[mid_p]:
                l_p = mid_p + 1
            elif nums[mid_p] <= nums[r_p]:
                r_p = mid_p - 1

        return -1

if __name__ == "__main__":
    sln = Solution()
    print(sln.search([3, 4, 5, 1, 2], 1))