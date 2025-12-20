# https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1136/
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        # Intuition: simply track if a stone is included
        # in jewels set.

        js = set()
        res = 0
        for j in list(jewels):
            js.add(j)
        for s in list(stones):
            if s in js:
                res += 1
        return res
        