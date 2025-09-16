# https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1661/
class Solution(object):
    cache = {}

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n
        if n in self.cache:
            return self.cache[n]
        
        res = self.fib(n - 1) + self.fib(n - 2)
        self.cache[n] = res
        return res
