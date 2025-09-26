# https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1131/
class Solution(object):
    def sq(self, n):
        s = 0
        while n > 0:
            # Resolve current digit
            digit = n % 10

            s += digit * digit

            # "Shift" the number to the right by 1
            # position.
            n //= 10
        return s

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Intuition:
        # Compute sum of squared digits
        # until the result of the computation
        # already exists in `seen` set - then
        # return `False`. If computation result
        # is `1`, return `True`.
        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.sq(n)
            if n == 1:
                return True
        return False
