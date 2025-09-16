# https://leetcode.com/problems/richest-customer-wealth/
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        res = 0
        for acc in accounts:
            acc_sum = 0
            for m in acc:
                acc_sum += m
            if (acc_sum > res):
                res = acc_sum
        return res
