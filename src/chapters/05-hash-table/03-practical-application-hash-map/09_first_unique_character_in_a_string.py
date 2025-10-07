# https://leetcode.com/problems/first-unique-character-in-a-string/submissions/1794313240/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Intuition:
        # Iterate the characters twice. First
        # count each char occurrences in a map.
        # Second run to find first char with single
        # occurrence.
        map = {}
        for i in range(len(s)):
            if s[i] in map:
                map[s[i]] += 1
            else:
                map[s[i]] = 1

        for i in range(len(s)):
            if map[s[i]] == 1:
                return i
        return -1
