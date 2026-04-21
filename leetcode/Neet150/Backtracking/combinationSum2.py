# Time Complexity: O(n*log n) + n^(t/n)*k
# Space Complexity: O(t/n) + O(n^(t/n))


class Solution:
    def combinationSum2(self, candidates: list, target: int) -> list:

        res = []
        candidates.sort()

        def dfs(
                nums_added: list,
                next_idx: int,
                sm: int,
                res: list,
        ) -> bool:


            if sm == target:
                res.append(nums_added.copy())
                return True

            if next_idx > len(candidates) - 1 or sm > target:
                return False

            seen = set()
            for i in range(next_idx, len(candidates)):

                if candidates[i] in seen:
                    continue
                else:
                    seen.add(candidates[i])

                nums_added.append(candidates[i])
                # next_idx += 1

                is_fine = dfs(nums_added, i + 1, sm + candidates[i], res)
                nums_added.pop()

                if not is_fine:
                    break

            return True

        dfs([], 0, 0, res)
        return res


if __name__ == "__main__":
    sln = Solution()
    print(sln.combinationSum2([1,2,3,4,5], 7))

