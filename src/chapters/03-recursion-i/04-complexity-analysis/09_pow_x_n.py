# https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/2380/
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1 / self.myPow(x, abs(n))
        elif n == 0:
            return 1
        elif n == 1:
            return x
        elif n % 2:
            # Caution: for odd `n` remember to multiply
            # by `x`.
            return self.myPow(x * x, n // 2) * x
        else:
            return self.myPow(x * x, n // 2)
