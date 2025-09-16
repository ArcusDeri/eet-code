# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Idea: set maximum to -1 - it will be used
        # to set the last element in the array as 
        # required. Iterate the array backwards, set
        # current element to maximum and check if
        # maximum should be updated.
        my_max = -1
        i = len(arr) - 1

        while i >= 0:
            # Use a temp variable so that we don't
            # lose potentially new maximum.
            maybe_next_max = arr[i]
            arr[i] = my_max
            my_max = max(my_max, maybe_next_max)
            i -= 1
        return arr
