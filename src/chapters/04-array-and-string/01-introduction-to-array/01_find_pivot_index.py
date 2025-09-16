# https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Intuition:
        # Sum all elements then decrease the sum
        # element by element while checking if both sums are equal.
        left_sum, right_sum = 0 ,0
        for n in nums:
            right_sum += n

        for i in range(len(nums)):
            # Important: decrease right side first to catch
            # edge cases like [2, -1, 1].
            right_sum -= nums[i]
            if right_sum == left_sum:
                return i
            left_sum += nums[i]
        return -1
