# https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Idea: two pointers climbing from both ends
        # should meet at the same peak in a valid
        # mountain array.
        if len(arr) < 3:
            return False
        left = 0
        right = len(arr) - 1

        while left < len(arr) - 1 and arr[left + 1] > arr[left]:
            left += 1
        
        while right > 1 and arr[right - 1] > arr[right]:
            right -= 1

        # Handle edge cases: when the array is a
        # single slope.
        if left == 0 or right == len(arr) - 1:
            return False
        return left == right
