# https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1135/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Intuition:
        # Use sliding window and a hashset.
        chars = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
        return res