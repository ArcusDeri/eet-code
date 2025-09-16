# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Idea: get the result quickly by using bitwise
        # shift instead of usual division - shifting to the
        # right by one is the same as dividing by two.
        # Use bitwise `&` to check parity.
        steps = 0

        while num != 0:
            if num &  1:
                # Odd, subtract
                num -= 1
            else:
                # Even, shift by one (divide by two)
                num >>= 1;
            steps += 1

        return steps
