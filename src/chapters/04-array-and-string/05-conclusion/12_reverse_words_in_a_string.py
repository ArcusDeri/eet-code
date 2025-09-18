# https://leetcode.com/problems/reverse-words-in-a-string/description/
class Solution(object):
    def remove_spaces(self, chars):
        left, right = 0, 0
        length = len(chars)

        while right < length:
            # Skip spaces
            while right < length and chars[right] == ' ':
                right += 1

            # Move the word to the left
            while right < length and chars[right] != ' ':
                chars[left] = chars[right]
                left += 1
                right += 1

            # Skip trailing spaces
            while right < length and  chars[right] == ' ':
                right += 1

            # Important detail: if there are more chars
            # yet then insert single space between the words.
            # Without it there will be no spaces between them.
            # E.g. consider input '  a  b '. This function
            # would return 'ab' instead of 'a b'.
            if right < length:
                chars[left] = ' '
                left += 1
        # Return all characters from the beginning up to `left`
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
        # Intuition:
        # Using trim and split functions make the problem
        # trivial but the desired solution is a bit
        # more complex: 
        # 0. convert string to char array
        # 1. remove excessive spaces
        # 2. reverse entire array
        # 3. reverse each word

        chars = self.remove_spaces(list(s))
        
        self.rev(chars, 0, len(chars) - 1)
    
        # reverse words
        start = 0
        for i in range(len(chars) + 1):
            if i == len(chars) or chars[i] == ' ':
                self.rev(chars, start, i - 1)
                start = i + 1
        return ''.join(chars)
