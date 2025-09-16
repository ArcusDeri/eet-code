# https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3234/
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        prev = self.getRow(rowIndex - 1)
        result = [1] * (rowIndex + 1)
        for i in range(1, rowIndex):
            result[i] = prev[i - 1] + prev[i]
        
        return result