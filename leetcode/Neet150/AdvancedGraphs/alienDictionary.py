from collections import defaultdict, deque
from typing import List

# Approach: Topological Sort
# C - amount of unique characters in a list of words.
# TC -> O(C)
# SC -> O(C)


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adjacency_list = defaultdict(set)
        freq_map = {}

        # Adjacency list
        for i in range(len(words)):
            for char in words[i]:
                if char not in freq_map:
                    freq_map[char] = 0

            if i - 1 >= 0:
                prev_word = words[i - 1]
                curr_word = words[i]
                min_len = min(len(prev_word), len(curr_word))
                is_changed = False
                for j in range(min_len):
                    if curr_word[j] == "t":
                        pass
                    if curr_word[j] in adjacency_list[prev_word[j]]:
                        is_changed = True
                        break
                    if prev_word[j] != curr_word[j]:
                        is_changed = True
                        freq_map[curr_word[j]] += 1
                        adjacency_list[prev_word[j]].add(curr_word[j])
                        break

                if not is_changed and len(curr_word) < len(prev_word):
                    return ""

        queue_list = []
        for k, v in freq_map.items():
            if v == 0:
                queue_list.append(k)

        queue = deque(queue_list)

        res = []
        while queue:
            left_e = queue.popleft()
            res.append(left_e)
            for child in adjacency_list[left_e]:
                freq_map[child] -= 1
                if freq_map[child] == 0:
                    queue.append(child)


        # Check for the cycle in the end
        for k, v in freq_map.items():
            if v > 0: return ""

        return "".join(res)

if __name__ == "__main__":
    sln = Solution()
    words=["wrt","wrf","er","ett","rftt","te"]
    print(sln.foreignDictionary(words))