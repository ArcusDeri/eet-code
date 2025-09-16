# https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1160/
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        aPtr, bPtr = len(a) - 1, len(b) - 1
        result = ''
        while aPtr >= 0 or bPtr >= 0:
            v = carry
            carry = 0
            if aPtr >= 0:
                v += int(a[aPtr])
                aPtr -= 1
            if bPtr >= 0:
                v += int(b[bPtr])
                bPtr -= 1
            
            if v < 2:
                result = str(v) + result
            elif v == 2:
                result = '0' + result
                carry = 1
            elif v == 3:
                result = '1' + result
                carry = 1

        if carry:
            result = '1' + result
        return result
