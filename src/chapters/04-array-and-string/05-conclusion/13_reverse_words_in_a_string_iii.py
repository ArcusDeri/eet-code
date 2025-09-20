# https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1165/
class Solution(object):
    def rev(self, chars, start, end):
        while start < end:
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Intuition:
        # Iterate characters until a space is matched.
        # then reverse a word and set helper pointer
        # to `i + 1` to point at next word start.
        start = 0
        chars = list(s)
        for i in range(len(chars) + 1):
            if i == len(chars) or chars[i] == ' ':
                self.rev(chars, start, i - 1)
                start = i + 1
        return ''.join(chars)
