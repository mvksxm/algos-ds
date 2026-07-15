from typing import List
from collections import deque

# m -> len(board); n -> len(board[0])
# TC -> O(m*n)
# SC - O(m*n) + O(m*n) = O(m*n)

class Solution:

    def solve(self, board: List[List[str]]) -> None:

        q = deque()
        visited_set = set()

        move_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (
                    (r == 0 or r == len(board) - 1 or c == 0 or c == len(board[0]) - 1)
                    and board[r][c] == "O"
                ):
                    q.append((r, c))
                    visited_set.add((r, c))

        while q:
            queue_elem = q.popleft()

            for direction in move_directions:
                next_r, next_c = queue_elem[0] + direction[0], queue_elem[1] + direction[1]
                if (
                        -1 < next_r < len(board)
                        and -1 < next_c < len(board[0])
                        and (next_r, next_c) not in visited_set
                        and board[next_r][next_c] == "O"
                ):
                    q.append((next_r, next_c))
                    visited_set.add((next_r, next_c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r, c) not in visited_set:
                    board[r][c] = "X"