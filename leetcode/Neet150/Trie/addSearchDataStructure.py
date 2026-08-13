
# n -> len(word)
# TC addWord -> O(n)
# TC search -> O(26^n)

# t -> total number of nodes in a trie
# SC -> O(t+n); n is for the length of the recursion stack.

class TrieNode:
    def __init__(self, children = None, is_word = False):

        if not children:
            children = {}

        self.children = children
        self.is_word = is_word


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:

        # Initial setup
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                node.children[word[i]] = TrieNode()
            node = node.children[word[i]]

        node.is_word = True

    def _recursive_search(self, node, word, idx):

        # Base case
        if idx == len(word) and node.is_word:
            return True

        if idx == len(word):
            return False

        char = word[idx]
        if char in node.children:
            if self._recursive_search(node.children[char], word, idx + 1):
                return True

        if char == ".":
            for child in node.children.values():
                if self._recursive_search(child, word, idx + 1):
                    return True

        return False

    def search(self, word: str) -> bool:
        return self._recursive_search(self.root, word, 0)

if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bay")
    print(wd.search("b.."))
