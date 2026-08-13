from typing import List

# TC -> O(m * n * 4 * 3^t-1); m -> rows; n -> cols; 4 - 4 initial choices where to go with dfs; t -> len of the searched
# word.
# SC -> O(s); s -> sum of lens of all the words.

class TreeNode:
    def __init__(self, children = None, is_word = False):
        if not children:
            children = {}

        self.children = children
        self.is_word = is_word


class Trie:
    def __init__(self):
        self.root = TreeNode()

    def add(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TreeNode()
            node = node.children[ch]
        node.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        trie = Trie()
        for word in words:
            trie.add(word)
        first_chars = trie.root.children

        res = set()

        visited_nodes = set()
        def dfs(row, col, trie_object, found_word):

            if not len(board) > row > -1 or not len(board[0]) > col > -1 :
                return

            if (row, col) in visited_nodes:
                return

            t_children = trie_object.children
            next_char = board[row][col]

            if next_char not in t_children:
                return

            found_word.append(next_char)
            visited_nodes.add((row, col))
            next_trie_object = t_children[next_char]

            if next_trie_object.is_word:
                res.add("".join(found_word))

            for dr in directions:
                dfs(row + dr[0], col + dr[1], next_trie_object, found_word)

            if not next_trie_object.children:
                del t_children[next_char]

            found_word.pop()
            visited_nodes.remove((row, col))


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in first_chars:
                    dfs(i, j, trie.root, [])

        return [wd for wd in res]


if __name__ == "__main__":
    sln = Solution()
    board=[["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
    words=["oa","oaa"]
    print(sln.findWords(board, words))