# https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1170/
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Intuition:
        # Basic, recursive approach.
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        prevs = self.generate(numRows - 1)
        prev = prevs[numRows - 2]
        current = [1] * numRows

        for i in range(1, numRows - 1):
            current[i] = prev[i - 1] + prev[i]

        prevs.append(current)

        return prevs
