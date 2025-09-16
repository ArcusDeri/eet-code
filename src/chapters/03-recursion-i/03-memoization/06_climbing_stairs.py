# https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1662/
class Solution(object):
    cache = {}

    def climbStairs(self, n: int) -> int:
        # Intuition:
        # Sketch the problem in form of a decision tree.
        # Number of "routes" is the solution and it turns
        # out to be the n-th number in Fibonacci sequence.
        if n < 4:
            return n
        elif n in self.cache:
            return self.cache[n]

        res = self.climbStairs(n - 2) + self.climbStairs(n - 1)
        self.cache[n] = res
        return res
