# https://leetcode.com/problems/reverse-words-in-a-string/description/
class Solution(object):
    def remove_spaces(self, chars):
        left, right = 0, 0
        length = len(chars)

        while right < length:
            while right < length and chars[right] == ' ':
                right += 1

            while right < length and chars[right] != ' ':
                chars[left] = chars[right]
                left += 1
                right += 1

            while right < length and  chars[right] == ' ':
                right += 1
            
            if right < length:
                chars[left] = ' '
                left += 1
        return chars[:left]

    def rev(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = self.remove_spaces(list(s))
        
        self.rev(chars, 0, len(chars) - 1)
    
        start = 0
        for i in range(len(chars) + 1):
            if i == len(chars) or chars[i] == ' ':
                self.rev(chars, start, i - 1)
                start = i + 1
        return ''.join(chars)
