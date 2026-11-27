from collections import deque

# n -> amount of rows/cols
# TC -> O(n^2)
# SC -> O(n^2)

class Solution:


    def calculateCoordinate(self, idx, n):
        whole_num = idx // n
        remainder = idx % n
        modifier = whole_num if not remainder else whole_num + 1

        row = n - modifier
        col = 0

        if modifier % 2 != 0 and not remainder:
            col = n - 1
        elif modifier % 2 == 0 and not remainder:
            col = 0
        elif modifier % 2 != 0:
            col = remainder - 1
        elif modifier % 2 == 0:
            col = n - remainder

        return row, col

    def snakesAndLadders(self, board: list[list[int]]) -> int:
        visited_set = set()
        n = len(board)
        queue = deque([(1, 0)]) # idx, dice_rolls

        while queue:
            idx, dice_rolls = queue.popleft()

            if idx == n*n: return dice_rolls

            last_allowed = min(idx + 6, n * n)

            for i in range(idx + 1, last_allowed + 1):

                row, col = self.calculateCoordinate(i, n)
                next_idx = board[row][col] if board[row][col] != -1 else i

                if next_idx not in visited_set:
                    queue.append((next_idx, dice_rolls + 1))

                visited_set.add(next_idx)

        return -1