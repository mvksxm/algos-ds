from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        res = 0

        for i in range(len(heights)):
            last_idx = i
            while stack and stack[-1][0] >= heights[i]:
                last_val, last_idx = stack.pop()
                res = max(res, last_val * (i - last_idx))

                if not stack:
                    last_idx = 0
                    break

            stack.append((heights[i], last_idx))

        while stack:
            num, idx = stack.pop()
            amount_left = len(heights) - idx
            res = max(res, num * amount_left)

        return res

if __name__ == "__main__":
    sln = Solution()
    print(sln.largestRectangleArea([1,1]))