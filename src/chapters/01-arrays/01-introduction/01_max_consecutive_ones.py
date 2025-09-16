# https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        current_streak = 0

        for num in nums:
            if num is 0:
                result = current_streak if current_streak > result else result
                current_streak = 0
            else:
                current_streak += 1

        return current_streak if current_streak > result else result
