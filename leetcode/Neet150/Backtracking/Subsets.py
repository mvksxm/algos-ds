class Solution:
    def subsets(self, nums: list) -> list:

        res = []

        def dfs(num_arr: list, nums_to_iterate: list, res: list):
            if not nums_to_iterate:
                res.append(num_arr)
                return
            left_to_check = nums_to_iterate[1:] if len(nums_to_iterate) > 1 else []
            dfs(num_arr, left_to_check, res) # [1], [3]; [1]
            dfs(num_arr + [nums_to_iterate[0]], left_to_check, res) # [1, 2], [3]; [1,3]


        dfs([], nums, res)
        return res


if __name__ == "__main__":
    nums = [3,2,4,1]
    sln = Solution()
    print(sln.subsets(nums))