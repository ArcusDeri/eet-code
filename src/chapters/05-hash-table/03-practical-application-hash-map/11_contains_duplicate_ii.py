# https://leetcode.com/problems/contains-duplicate-ii/https://leetcode.com/problems/contains-duplicate-ii/
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Intuition:
        # Iterate and map current number to its index
        # If the number is in the map then check the
        # distance. No need to use `abs()` because we
        # always subtract from a higher index. No need
        # to check if subtraction gives 0 because we
        # will never get current index from the map
        # (it is: we always compare two distinct indices).
        m = {}
        for i in range(len(nums)):
            n = nums[i]
            if n in m and i - m[n] <= k:
                return True
            m[n] = i
        return False
                