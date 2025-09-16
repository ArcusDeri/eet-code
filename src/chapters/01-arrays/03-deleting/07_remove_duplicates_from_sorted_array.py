# https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Idea: iterate over `nums` and look for
        # values different than `nums[k]`. When
        # found, increment `k` first (to avoid
        # overwriting of `nums[0]` that shouldn't
        # be considered a duplicate), then copy
        # the value to `nums[k]`.
        # Return `k + 1` because `k` points at 
        # array index that is zero-based.
        k = 0
        for i in range(0, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return k + 1
