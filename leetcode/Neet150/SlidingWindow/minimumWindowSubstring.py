
from collections import deque

# Time Complexity: O(n); where n is the len(s)
# Space Complexity: O(n) + O(m); where n is the len(s) and m is the amount of unique chars in t.

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        chars_cnt = len(t)
        chars_hm = {}

        # Filling the map with counts of target chars
        for ch in t:
            if ch in chars_hm:
                chars_hm[ch] = chars_hm[ch] + 1
                continue
            chars_hm[ch] = 1

        # l_p = 0
        r_p = 0
        for i in range(len(s)):
            if s[i] in chars_hm:
                # l_p = i
                r_p = i
                break

        index_queue = deque()
        res_sub_left = -1
        res_sub_right = -1
        res_sub_cnt = float('inf')

        local_cnt = 0
        while r_p < len(s):

            if local_cnt == chars_cnt:
                l_p = index_queue.popleft()
                chars_hm[s[l_p]] = chars_hm[s[l_p]] + 1
                chars_needed = chars_hm[s[l_p]]
                if chars_needed > 0: local_cnt -= 1

                curr_sub_len = r_p - l_p + 1
                if curr_sub_len < res_sub_cnt:
                    res_sub_left = l_p
                    res_sub_right = r_p + 1
                    res_sub_cnt = curr_sub_len


                if local_cnt  == chars_cnt: continue

                r_p += 1
                continue

            if s[r_p] in chars_hm:
                chars_left = chars_hm[s[r_p]]
                if chars_left > 0: local_cnt += 1
                chars_hm[s[r_p]] = chars_hm[s[r_p]] - 1
                index_queue.append(r_p)

                # Additional if statement in order to not update the r_p
                if local_cnt == chars_cnt: continue

            r_p += 1

        if res_sub_left == -1 and res_sub_right == -1:
            return ""

        return s[res_sub_left:res_sub_right]

if __name__ == "__main__":
    sln = Solution()
    print(sln.minWindow("ADOBBCODEBANC", "ABC"))