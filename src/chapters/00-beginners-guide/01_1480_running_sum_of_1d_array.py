# https://leetcode.com/problems/running-sum-of-1d-array/
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        sum_so_far = 0
        for i in range(len(nums)):
            sum_so_far += nums[i]
            res[i] = sum_so_far
        
        return res
