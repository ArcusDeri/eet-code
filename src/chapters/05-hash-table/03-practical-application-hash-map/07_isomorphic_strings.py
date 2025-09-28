# https://leetcode.com/problems/isomorphic-strings/
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Intuition:
        # Use two dictionaries to check if a character
        # always maps to the same character and if mapped
        # character is mapped only by a single character
        # (e.g. in strings "bade" and "baca" 'a' is mapped
        # to 'a' but 'e' can't map to 'a' because 'a' is
        # already "taken").
        map_to = {} # 's' char maps to char in 't'
        map_from = {} # 't' char is mapped by 's' char
        for i in range(len(s)):
            if s[i] in map_to and map_to[s[i]] != t[i]:
                # 's' char already maps to a different character
                return False
            if t[i] in map_from and map_from[t[i]] != s[i]:
                # 't' char is already mapped by a diffeereent 's' char
                return False
            map_to[s[i]] = t[i]
            map_from[t[i]] = s[i]
        return True