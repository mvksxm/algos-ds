
# TC -> O(n * 26) = O(n)
# SC -> O(26) = O(1)


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        encoding = [0] * 26
        res = []

        for char in p:
            encoding[ord(char) - ord('a')] += 1

        p_len = len(p)
        l_p = -1

        for r_p in range(len(s)):
            l_p = r_p - p_len

            if l_p >= 0:
                encoding[ord(s[l_p]) - ord('a')] += 1

            encoding[ord(s[r_p]) - ord('a')] -= 1
            if not any(encoding):
                res.append(l_p + 1)

        return res