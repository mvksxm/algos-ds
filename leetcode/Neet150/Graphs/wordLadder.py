import string
from collections import deque
from typing import List


# TC -> O(m * n * 24) -> O(m * n)
# SC -> O(m * n * 24) -> O(m * n)
# Approach: bidirectional BFS

class Solution:

    # Initial approach
    def ladderLengthInitial(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        s_map = {beginWord: 1}
        e_map = {endWord: 1}
        w_list_set = set(wordList)

        # Initial check
        if endWord not in w_list_set:
            return 0

        min_words = float('inf')
        queue = deque([(beginWord, True), (endWord, False)])

        while queue:
            word, is_start = queue.popleft()

            if is_start and s_map[word] + 1 >= min_words:
                return min_words

            children = []
            for i in range(len(word)):
                for l in string.ascii_lowercase:
                    temp_word = word[:i] + l + word[i+1:]
                    if temp_word in w_list_set: children.append(temp_word)

            for ch in children:
                if is_start and ch in e_map:
                    min_words = min(min_words, s_map[word] + e_map[ch])

                if is_start and ch not in s_map:
                    s_map[ch] = s_map[word] + 1
                    queue.append((ch, True))

                if not is_start and ch in s_map:
                    min_words = min(min_words, e_map[word] + s_map[ch])

                if not is_start and ch not in e_map:
                    e_map[ch] = e_map[word] + 1
                    queue.append((ch, False))


        if min_words == float('inf'):
            return 0

        return min_words

    # Canonical version
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_list_set = set(wordList)
        if endWord not in word_list_set: return 0

        distance = 1
        end_set = {endWord}
        start_set = {beginWord}
        visited_set = set()

        while len(start_set) > 0 and len(end_set) > 0:
            if len(start_set) > len(end_set):
                start_copy = start_set
                start_set = end_set
                end_set = start_copy


            temp_set = set()
            for word in start_set:
                word_arr = list(word)
                for i in range(len(word_arr)):
                    old_char = word_arr[i]
                    for l in string.ascii_lowercase:
                        word_arr[i] = l
                        temp_str = "".join(word_arr)

                        if temp_str in end_set:
                            return distance + 1

                        if temp_str not in visited_set and temp_str in word_list_set:
                            temp_set.add(temp_str)
                            visited_set.add(temp_str)

                    word_arr[i] = old_char

            start_set = temp_set
            distance += 1

        return 0

if __name__ == "__main__":
    sln = Solution()
    beginWord="hit"
    endWord="cog"
    wordList=["hot","dot","tog","cog"]
    print(sln.ladderLength(beginWord, endWord, wordList))