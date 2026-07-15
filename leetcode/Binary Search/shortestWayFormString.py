from collections import defaultdict
from tester import Tester

# S -> source; T -> target
# TC -> T * log(S)
# SC -> O(S)

# Approach
# 1) Create a map where each character from source is a key and a value is an array of character's indexes in a source.
# 2) Iterate through target. If char in target is not in a map -> impossible case (return -1). Otherwise, execute Binary
# Search on a list of source indexes of a char encountered and search for the idx that is the smallest from the ones that
# are bigger than the latest one grabbed from source. If found -> swap last_idx with this idx, otherwise increment the
# result by 1 and set last_idx to the first index of the character in source.

def binary_search(arr, idx) -> int:

    l_p = 0
    r_p = len(arr) - 1

    first_bigger_idx = -1

    while l_p <= r_p:
        middle_p = l_p + (r_p - l_p) // 2

        if arr[middle_p] > idx:
            first_bigger_idx = arr[middle_p]
            r_p = middle_p - 1
        else:
            l_p = middle_p + 1

    return first_bigger_idx


def shortest_way_form_string(source: str, target: str) -> int:

    if not target: return 0

    index_map = defaultdict(list)

    for i in range(len(source)):
        index_map[source[i]].append(i)

    res = 1
    last_idx = -1
    for char in target:
        if char not in index_map: return -1

        next_idx = binary_search(index_map[char], last_idx)

        if next_idx == -1:
            last_idx = index_map[char][0]
            res += 1
        else:
            last_idx = next_idx

    return res


if __name__ == "__main__":

    s = "abcabc"
    t = "ccbaac"

    tst = Tester()
    test_list = [
        # Basic examples
        [["abc", "abcbc"], 2],
        [["abc", "abca"], 2],
        [["abc", "acdbc"], -1],
        [["xyz", "xzyxz"], 3],

        # Exact match
        [["abc", "abc"], 1],

        # Empty target
        [["abc", ""], 0],

        # Single character source
        [["a", "a"], 1],
        [["a", "aaaa"], 4],
        [["a", "b"], -1],

        # Repeated subsequences
        [["abc", "abcabc"], 2],
        [["abc", "abcabcabc"], 3],

        # Restart required
        [["abc", "cab"], 2],
        [["abc", "bcab"], 2],
        [["abc", "cba"], 3],

        # Missing character
        [["abc", "abcd"], -1],
        [["abc", "d"], -1],
        [["abc", "aaaaad"], -1],

        # Duplicate letters in source
        [["abca", "aaaa"], 2],
        [["abca", "aacaa"], 3],
        [["abac", "aaac"], 2],
        [["ababa", "aaa"], 1],
        [["ababa", "aaaaaa"], 2],

        # Order matters
        [["abcdef", "fed"], 3],
        [["abcdef", "face"], 2],

        # Long repeated targets
        [["abc", "abababab"], 4],
        [["ab", "ababababab"], 5],
        [["abc", "cccccccc"], 8],

        # Multiple occurrences
        [["aabbcc", "abccba"], 3],
        [["aabbcc", "abc"], 1],
        [["aabbcc", "cccc"], 2],

        # Greedy pitfalls
        [["baa", "aaab"], 3],
        [["bacab", "aab"], 1],
        [["abba", "baba"], 2],

        # Large repeated patterns
        [["abcdef", "abcdefabcdefabcdef"], 3],
        [["abcabc", "ccbaac"], 3],

        # Impossible cases
        [["abca", "aaaad"], -1],
        [["leetcode", "codeleetz"], -1],

        # Source equals target
        [["leetcode", "leetcode"], 1],

        # Character appears only at the end
        [["zzza", "aaaa"], 4],

        # Character appears only at the beginning
        [["abbb", "aaaa"], 4],
    ]

    tst.array_test(test_list, shortest_way_form_string)
