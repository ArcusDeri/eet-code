# https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1176/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Intuition:
        # One way is to use hash set for help.
        # Another is to use XOR operation on all
        # numbers. Duplicates cancel out even
        # if they aren't coming one by one because
        # XOR is associative. It means that for
        # example: A ^ B ^ C = C ^ A ^ B ( in other
        # words the order doesn't matter). Then
        # whatever remains is the seeked result.
        res = 0
        for n in nums:
            res ^= n
        return res
