# https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/1675/
class Solution(object):
    def powerOfTwo(self, n):
        if n == 0:
            return 1
        return 2 << (n - 1)

    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # Intuition:
        # Reduce the problem with recursion until `k` becomes 1.
        # Observe that every next row is like negated previous
        # row. If `k` is greater than previous row length, subtract
        # that length from `k` and get the symbol for that `k'`
        # in previous row. Remember to negate the result.
        # Otherewise simply get k-th symbol in previous row.
        if k == 1:
            return 0
        # Length of n - 1 row.
        # Length if n-th row is 2^(n-1) so
        # previous row length is 2^(n-1-1).
        prew_row_length = self.powerOfTwo(n - 2)
        if k > prew_row_length:
            return self.kthGrammar(n - 1, k - prew_row_length) ^ 1
        else:
            return self.kthGrammar(n - 1, k)
