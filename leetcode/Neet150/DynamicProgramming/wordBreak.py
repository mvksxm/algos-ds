from collections import deque
from typing import List


# n -> len(s); k -> longest word in a wordDict; m -> len(wordDict)
# Trie-based solution
# TC -> O(n * k) + O(m * k);
# SC -> O(m * k)

# DP-based solution
# TC -> O(n^2)
# SC -> O(n + m)

# Trie-based solution
# Approach: create a Trie and place all the words from the wordDict there. Afterward, iterate through the string 's'
# and in parallel traverse through the Trie. In case, if word is encountered in a Trie -> add next_idx (i+1 of 's') to
# the queue, so that traversal could be restarted from the root node of the Trie and from the next_idx of 's'. Also,
# in case if next_idx was already visited, we are skipping it, because we assume the processing from this particular
# element -> s[next_idx] is already ongoing and there is no need to restart it.
# In case, if we encounter a word in a Trie and current char_idx == len(nums) - 1, we return True right away, because
# we assume that we were able to reach to the end by using the words in a Trie. Otherwise, in case if True condition
# had never been triggered, we can assume that we can't reach the end of s by using words from wordDict, so we return
# 'False'.

# DP-based solution (recursive with memoization)
# We iterate through string - 's' and constantly checking if s[i:j + 1] is in the word_set (set copy of the wordDict).
# In case if it is and j + 1 not in dp (we didn't compute it previously), we are performing a recursive call dfs(j+1),
# which checks if the substr starting from the j + 1 is present in the word_set. Operation is repeated until the max
# depth of recursion is reached, which can be as big as len(s). On return, we are inputting placing idx:bool into the
# dp map, which states if it's possible to reach the end from this particular idx by using words from the wordDict. dp
# map is used afterward in order to not repeat the recursive operations for the indexes, which were already computed.


class TrieNode:
    def __init__(self, children = None, is_word = False):
        if not children:
            children = {}

        self.children = children
        self.is_word = is_word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str):
        curr_node = self.root
        for ch in word:
            if ch not in curr_node.children:
                curr_node.children[ch] = TrieNode()
            curr_node = curr_node.children[ch]
        curr_node.is_word = True


class Solution:

    # BFS + Trie-based solution.
    def wordBreakTrie(self, s: str, wordDict: List[str]) -> bool:

        # Create a trie
        trie = Trie()
        for word in wordDict:
            trie.add_word(word)

        queue = deque([0])
        visited = {0}

        while queue:
            char_idx = queue.popleft()
            node = trie.root
            char = s[char_idx]

            while char in node.children:

                node = node.children[char]
                if node.is_word and char_idx == len(s) - 1:
                    return True

                next_char_idx = char_idx + 1
                if (
                        node.is_word and next_char_idx not in visited
                        and next_char_idx < len(s)
                ):
                    queue.append(next_char_idx)
                    visited.add(next_char_idx)

                char = s[next_char_idx] if next_char_idx < len(s) else ""
                char_idx = next_char_idx

        return False

    # DP Solution
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_set = {word for word in wordDict}
        dp = {}

        def dfs(i):

            if i in dp:
                return dp[i]

            if i >= len(s):
                return True

            for j in range(i, len(s)):
                curr_str = s[i:j+1]
                if curr_str in word_set and j + 1 in dp and dp[j + 1]:
                    return dp[j + 1]
                if curr_str in word_set:
                    if dfs(j + 1):
                        dp[i] = True
                        return True

            dp[i] = False
            return False

        return dfs(0)




if __name__ == "__main__":
    sln = Solution()
    s = "catsincars"
    wordDict =  ["cats","cat","sin","in","cars"]
    print(sln.wordBreak(s, wordDict))