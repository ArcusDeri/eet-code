# https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = None
        second = None
        third = None
        for n in nums:
            if n == first or n == second or n == third:
                continue

            if first == None or n > first:
                third = second
                second = first
                first = n
            elif second == None or n > second:
                third = second
                second = n
            elif third == None or n > third:
                third = n
        if third == None:
            return first
        return third