class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        for num in nums:
            if num > 9 and num < 100 or num > 999 and num < 10000 or num > 99999:
                count += 1

        return count
