# https://leetcode.com/problems/intersection-of-two-arrays/submissions/1782383325/
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Intuition:
        # Save elements of one array in a map,
        # then iterate second array and check
        # if current element exists in the map.
        # If so, add it to the result array.
        map = {}
        for n in nums1:
            map[n] = True
        res = []
        for n in nums2:
            if n in map:
                res.append(n)
                map.pop(n)
        return res
