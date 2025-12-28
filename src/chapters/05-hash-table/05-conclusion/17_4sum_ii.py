# https://leetcode.com/problems/4sum-ii/submissions/1867855102/
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        # Intuition:
        # Iterate nums1 and nums2, store frequencies of
        # sums of each element combination from both collections.
        # Then iterate nums3 and nums4 while looking for presence
        # of "negative sum" of elements in the map. Add frequency
        # count to output variable.
        m = {}
        for a in nums1:
            for b in nums2:
                m[a + b] = m.get(a + b, 0) + 1
        r = 0

        for c in nums3:
            for d in nums4:
                # a + b + c + d = 0 => a + b = -(c + d)
                s = -(c + d)
                if s in m:
                    r += m[s]
        return r
