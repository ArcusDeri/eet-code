# https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        maxDouble = 0
        maxIdx = 0
        for i in range(len(nums)):
            if nums[i] > max:
                maxDouble = max * 2
                max = nums[i]
                maxIdx = i
            elif nums[i] * 2 > maxDouble:
                maxDouble = nums[i] * 2
        
        if nums[maxIdx] >= maxDouble:
            return maxIdx
        else:
            return -1