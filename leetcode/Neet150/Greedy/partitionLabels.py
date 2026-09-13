from collections import defaultdict
from typing import List

# TC -> O(n)
# SC -> O(1), since alphabet's len is fixed - 26 chars.

# Approach
# Maintain a global frequency map - freq_map and per partition set - 'visited_set'. Start iteration through s.
# Add character encountered to the visited_set and also decrement a count of this character in the frequency map.
# If frequency of character encountered is 0 -> remove it from the set. At the end of each iteration - check if
# visited_set is empty, if it is -> add current count to the res array and update count to 0.

class Solution:

    # My implementation with the visited set
    def partitionLabels(self, s: str) -> List[int]:

        if len(s) == 1: return [1]

        freq_map = defaultdict(int)
        for ch in s:
            freq_map[ch] += 1

        res = []
        count = 0
        visited_set = set()
        for i in range(len(s)):

            freq_map[s[i]] -= 1
            visited_set.add(s[i])
            count += 1

            if freq_map[s[i]] == 0:
                visited_set.remove(s[i])

            if not visited_set:
                res.append(count)
                count = 0

        return res


if __name__ == "__main__":
    sln = Solution()
    print(sln.partitionLabels("aabccdeff"))