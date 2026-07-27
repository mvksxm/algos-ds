from typing import List


# TC -> O(4^n)
# SC -> O(n)

class Solution:

    def addOperators(self, num: str, target: int) -> List[str]:

        res = []

        def dfs(idx, sm, pattern, prev_number):

            if idx >= len(num) and sm == target:
                res.append(pattern[1:])
                return

            if idx >= len(num):
                return

            for i in range(idx, len(num)):

                next_num = num[idx:i+1]
                next_num_int = int(next_num)

                # Sum
                dfs(i+1, sm + next_num_int, pattern + "+" + next_num, next_num_int)

                # Sub
                if idx > 0: dfs(i+1, sm - next_num_int, pattern + "-" + next_num, -next_num_int)

                # Multiplication
                if idx > 0: dfs(i+1, sm - prev_number + prev_number * next_num_int, pattern + "*" + next_num, prev_number * next_num_int)

                if num[idx] == "0": break

        dfs(0, 0, "", num[0])

        return res




if __name__ == "__main__":
    sln = Solution()
    print(sln.addOperators("232", 8))