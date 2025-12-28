# https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1133/
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Intuition:
        # To maintain O(n) time and space complexity we
        # need three loops:
        # 1. store frequencies in a map
        # 2. assign numbers to "frequency buckets"
        # 3. collect results from buckets
        m = {}
        buckets = [set() for _ in range(len(nums))]

        for n in nums:
            m[n] = m.get(n, 0) + 1
        for ke, v in m.items():
            if ke not in buckets[v - 1]:
                buckets[v - 1].add(ke)
        res = []
        r = len(buckets) - 1
        while k > 0:
            for n in buckets[r]:
                res.append(n)
                k -= 1
            r -= 1
        return res
