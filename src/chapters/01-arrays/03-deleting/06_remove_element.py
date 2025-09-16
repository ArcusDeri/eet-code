# https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Idea: `k` serves as a "slow pointer".
        # Copy elements to `nums[k]`` only if they aren't
        # equal to `val`. Increment k on copy.
        k = 0

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k
