# https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1178/
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Intuition:
        # Count occurrences of numbers in nums1.
        # Iterate the second list and append `n`
        # as long as it's in the map and mapped
        # value is higher than 0.
        freq = {}
        for n in nums1:
            freq[n] = freq.get(n, 0) + 1
        
        res = []

        for n in nums2:
            if n in freq and freq[n] > 0:
                res.append(n)
                freq[n] -= 1
        return res
            