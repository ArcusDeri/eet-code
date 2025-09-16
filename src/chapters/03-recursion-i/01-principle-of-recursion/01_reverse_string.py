# https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1440/
class Solution(object):
    def revInner(self, arr, left, right):
        if left >= right:
            return
        
        arr[left], arr[right] = arr[right], arr[left]
        self.revInner(arr, left + 1, right - 1)

    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # Intuition:
        # Swap first character with last, then continue recursively
        # towards the middle.
        self.revInner(s, 0, len(s) - 1)
