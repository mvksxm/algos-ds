from typing import List


# Approach -> backtracking
# n = len(digits);
# TC -> O(4^n)
# SC -> O(n)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits: return []

        digit_map = {
            "2":"abc", "3":"def","4":"ghi",
            "5":"jkl", "6":"mno","7":"pqrs",
            "8":"tuv", "9":"wxyz"
        }

        res = []

        def dfs(idx: int, letters: list):
            if idx >= len(digits):
                res.append("".join(letters))
                return

            digit_letters = digit_map[digits[idx]]

            for dg in digit_letters:
                letters.append(dg)
                dfs(idx + 1, letters)
                letters.pop()

        dfs(0, [])

        return res