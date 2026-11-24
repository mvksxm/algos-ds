
# TC -> O(m * n)
# SC -> O(1)


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        DIRS =  (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)


        for r in range(len(board)):
            for c in range(len(board[0])):

                neighbours = 0

                cell = board[r][c]

                for r_m, c_m in DIRS:
                    if r_m == -1 and c_m == 1:
                        pass
                    r_n, c_n = r + r_m, c + c_m

                    if (
                            (0 <= r_n < len(board))
                            and (0 <= c_n < len(board[0]))
                            and (board[r_n][c_n] == 1 or board[r_n][c_n] == 2)
                    ):
                        neighbours += 1

                if cell == 0 and neighbours == 3:
                    board[r][c] = 3
                elif cell == 1 and (neighbours > 3 or neighbours < 2):
                    board[r][c] = 2


        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1

if __name__ == "__main__":
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    sln = Solution()
    sln.gameOfLife(board)
    print(board)
