
# Trie (Prefix Tree) data structure

# n -> len(word)
# TC (search) -> O(n)
# TC (insert) -> O(n)

# t -> amount of nodes in the trie (26 per level at max)
# SC -> O(t)


class TreeNode:
    def __init__(self, children=None, is_word = False):
        if children is None:
            children = {}
        self.children = children
        self.is_word = is_word

class Trie:

    def __init__(self):
        self.root = TreeNode()


    def _recursive_insert(self, node, char_list):

        if not char_list:
            node.is_word = True
            return

        first_char = char_list.pop()

        if first_char in node.children:
            self._recursive_insert(node.children[first_char], char_list)
            return

        child_node = TreeNode()
        node.children[first_char] = child_node
        self._recursive_insert(child_node, char_list)

    def _iterative_insert(self, word):
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                node.children[word[i]] = TreeNode()
            node = node.children[word[i]]

        node.is_word = True

    def insert(self, word: str) -> None:
        self._iterative_insert(word)

    def _search(self, word, is_prefix = False):
        node = self.root

        for i in range(len(word)):
            if word[i] not in node.children:
                return False

            node = node.children[word[i]]

        if not node.is_word and not is_prefix:
            return False

        return True


    def search(self, word: str) -> bool:
        return self._search(word)

    def startsWith(self, prefix: str) -> bool:
        return self._search(prefix, True)


if __name__ == "__main__":
    tr = Trie()
    print(tr.startsWith("a"))