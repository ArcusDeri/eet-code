# https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1177/
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # Intuition:
        # store indices of elements of one list in a dictionary.
        # Then iterate the second list and check if each string exists
        # in the dictionary. Calculate index sum, if it's lower
        # than current sum then reset the result list.
        # If it's equal then just add the string.
        res = []
        min_sum = len(list1) + len(list2)
        first = {}
        for i in range(len(list1)):
            first[list1[i]] = i
        for i in range(len(list2)):
            s = list2[i]
            if s in first:
                s_sum = i + first[s]
                if s_sum < min_sum:
                    min_sum = s_sum
                    res = [s]
                elif s_sum == min_sum:
                    res.append(s)
        return res
