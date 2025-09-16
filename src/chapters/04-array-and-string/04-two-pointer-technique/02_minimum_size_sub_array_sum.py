# https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1299/
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # The idea is to use a sliding window.

        # length + 1 here to make it easier with recognizing
        # if there is no target sub array when returning the result
        result = len(nums) + 1
        left, right = 0, 0
        currentSum = 0
        while right < len(nums):
            # Extend the window
            currentSum += nums[right]
            while currentSum >= target:
                # Target reached, update the result if necessary
                result = min(result, right - left + 1)
                # Shrink the window
                currentSum -= nums[left]
                left += 1
            right += 1

        return result if result <= len(nums) else 0


