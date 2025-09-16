# https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        right = len(nums) - 1
        left = 0
        result = [0] * len(nums)
        i = len(nums) - 1
        while i >= 0:
            lvalue = abs(nums[left])
            rvalue = abs(nums[right])
            if lvalue < rvalue:
                result[i] = rvalue * rvalue
                right -= 1
            else:
                result[i] = lvalue * lvalue
                left += 1
            i -= 1

        return result
