
# n -> height of the triangle (also a length of the bottom row)
# TC -> O(n^2)
# SC -> O(n)

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        path_sum = triangle[0] + [float('inf')] * (len(triangle) - 1)

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i]) - 1, -1, -1):
                left_top = float('inf') if j - 1 < 0 else path_sum[j - 1]
                min_sum = min(left_top + triangle[i][j], path_sum[j] + triangle[i][j])
                path_sum[j] = min_sum

        return min(path_sum)


if __name__ == "__main__":
    sln = Solution()
    print(sln.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))