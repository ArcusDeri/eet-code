# https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Idea: iterate over the array and
        # save each element in a dictionary.
        # If a given element's double is already 
        # present in the dictionary, return True.
        # If given element is even and its half 
        # is already in the dictionary, return True.
        lookup = {}
        for n in arr:
            if n * 2 in lookup or (n % 2 == 0 and n // 2 in lookup):
                return True
            
            lookup[n] = n

        return False
