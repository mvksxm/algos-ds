from typing import List

# n -> len(s)
# d -> max(dictionary[i]
# m -> len(dictionary)

# Approach: DP + Trie
# TC -> O(n^2)
# SC -> O(n + m * d)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = TrieNode()
                node = node.children[char]

        node.is_word = True

    def search_subset(self, word, idx, dp):
        min_left = float('inf')

        node = self.root
        for i in range(idx, len(word)):
            char = word[i]
            if char not in node.children:
                break

            node = node.children[char]
            if node.is_word and dp[i + 1] < min_left:
                min_left = dp[i + 1]

        return min_left



class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        trie = Trie()

        # Load the words
        for word in dictionary:
            trie.add(word)

        dp = [float('inf')] * (len(s) + 1)
        dp[-1] = 0

        for i in range(len(s) - 1, -1, -1):
            min_left = trie.search_subset(s, i , dp)
            dp[i] = min(1 + dp[i + 1], min_left)

        return dp[0]