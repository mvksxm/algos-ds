from typing import List

# m -> len(matrix); n -> len(matrix[0])
# TC -> O(m * n)
# SC -> O(1)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        t_r = 0
        l_c = 0
        r_c = len(matrix[0]) - 1
        b_r = len(matrix) - 1


        while t_r < b_r and l_c < r_c:

            # top iteration
            for c in range(l_c, r_c + 1):
                res.append(matrix[t_r][c])

            # right iteration
            for r in range(t_r + 1, b_r + 1):
                res.append(matrix[r][r_c])

            # bottom iteration
            for c in range(r_c - 1, l_c - 1, -1):
                res.append(matrix[b_r][c])

            # left iteration
            for r in range(b_r - 1, t_r, -1):
                res.append(matrix[r][l_c])


            t_r += 1
            l_c += 1
            r_c -= 1
            b_r -= 1

        if t_r == b_r:
            for c in range(l_c,r_c+1):
                res.append(matrix[t_r][c])

        if l_c == r_c:
            for r in range(t_r,b_r + 1):
                res.append(matrix[r][l_c])

        return res

if __name__ == "__main__":
    sln = Solution()
    print(sln.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

