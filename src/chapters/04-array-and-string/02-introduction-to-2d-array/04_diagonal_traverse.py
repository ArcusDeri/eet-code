# https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        # Intuition:
        # Use a flag for "direction" (up or down).
        # If bounds are reached change the direction and set position
        # properly.
        m_rows, n_cols = len(mat), len(mat[0])
        mm, nn = 0, 0 # "current" position in the matrix
        bound_top, bound_bot = 0, m_rows - 1
        bound_left, bound_right = 0, n_cols - 1
        result = [0] * m_rows * n_cols

        going_up = True
        for i in range(m_rows * n_cols):
            result[i] = mat[mm][nn]
            if going_up:
                # First check the right edge to handle situation
                # where we land exactly in the upper right corner.
                if nn == bound_right:
                    going_up = False
                    mm += 1
                elif mm == bound_top:
                    going_up = False
                    nn += 1
                else:
                    mm -= 1
                    nn += 1
            else:
                # First check the botton edge to handle situation
                # where we land exactly in the bottom left corner.
                if mm == bound_bot:
                    going_up = True
                    nn += 1
                elif nn == bound_left:
                    going_up = True
                    mm += 1
                else:
                    mm += 1
                    nn -= 1
        return result