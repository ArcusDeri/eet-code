# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Idea: swap elements when even number is found.
        # `left` is a "slow" pointer while `right` goes faster.
        left = 0
        for right in range(len(nums)):
            if nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return nums
