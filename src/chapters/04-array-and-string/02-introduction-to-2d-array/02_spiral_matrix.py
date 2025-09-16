# https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1168/
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Intuition:
        # Traverse using "speed" variables for row and column.
        # Change the speed when bounds are reached.
        mm, nn = 0, 0
        m_rows, n_cols = len(matrix), len(matrix[0])
        top, right, bottom, left = 0, n_cols - 1, m_rows - 1, -1
        result = [0] * m_rows * n_cols
        ptr = 0
        m_speed, n_speed = 0, 1
        while ptr < len(result):
            result[ptr] = matrix[mm][nn]
            ptr += 1
            if mm == top and nn == right:
                left += 1
                m_speed = 1
                n_speed = 0
            elif mm == bottom and nn == right:
                top += 1
                m_speed = 0
                n_speed = -1
            elif mm == bottom and nn == left:
                right -= 1
                m_speed = -1
                n_speed = 0
            elif mm == top and nn == left:
                bottom -= 1
                m_speed = 0
                n_speed = 1
            mm += m_speed
            nn += n_speed
        return result