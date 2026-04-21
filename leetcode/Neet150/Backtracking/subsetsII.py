from typing import List

# Time Complexity: nlogn +  2*n^n
# Space Complexity: n^n

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = [[]]
        nums.sort()

        def dfs(parent_structure: list, first_child_idx: int, res: list):

            if first_child_idx > len(nums) - 1:
                # res.append(parent_structure.copy())
                return

            dedup_set = set()
            for i in range(first_child_idx, len(nums)):

                if nums[i] in dedup_set:
                    continue
                else:
                    dedup_set.add(nums[i])

                parent_structure.append(nums[i])
                res.append(parent_structure.copy())
                dfs(parent_structure, i+1, res)
                parent_structure.pop()

        dfs([], 0, res)

        return res

if __name__ == "__main__":
    sln = Solution()
    print(sln.subsetsWithDup([7,7]))

