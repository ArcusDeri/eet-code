# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Idea: We use `zeroPtr` to track 
        # the position where the next non-zero
        # element should go. Every time we find
        # a non-zero number, we swap it with the
        # element at `zeroPtr`, and then move
        # `zeroPtr` one step forward. This 
        # effectively pushes all zeroes to the 
        # end of the list in a single pass.
        zeroPtr = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zeroPtr], nums[i] = nums[i], nums[zeroPtr]
                zeroPtr += 1

        return nums
