

# N -> len(strs)
# L -> max len of an element in strs array.

# TC -> O(N * L)
# SC -> O(N * L)

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp = {}

        for st in strs:
            encoding = [0] * 26
            for char in st:
                encoding[ord(char) - ord('a')] += 1

            encoding = tuple(encoding)

            if encoding in mp:
                mp[encoding].append(st)
            else:
                mp[encoding] = [st]


        return [val for _, val in mp.items()]


if __name__ == "__main__":
    sln = Solution()
    print(sln.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))