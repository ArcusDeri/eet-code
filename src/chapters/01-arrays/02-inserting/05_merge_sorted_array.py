# https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Idea: use two pointers to pick the greater value.
        # Fill in the result array from the back to avoid overwriting the values.
        mPtr = m - 1
        nPtr = n - 1
        resPtr = len(nums1) - 1

        # Both pointers point to valid indexes, compare the values.
        # Pick the larger value and insert to result index.
        while mPtr >= 0 and nPtr >= 0:
            if nums1[mPtr] > nums2[nPtr]:
                nums1[resPtr] = nums1[mPtr]
                mPtr -= 1
            else:
                nums1[resPtr] = nums2[nPtr]
                nPtr -= 1
            resPtr -= 1
        
        # Copy remaining values from nums1
        while mPtr >= 0:
            nums1[resPtr] = nums1[mPtr]
            mPtr -= 1
            resPtr -= 1
        
        # Copy remaining values from nums2
        while nPtr >= 0:
            nums1[nPtr] = nums2[nPtr]
            nPtr -= 1
            resPtr -= 1
