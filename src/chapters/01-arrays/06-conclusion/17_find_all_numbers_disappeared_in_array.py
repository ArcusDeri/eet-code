# https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Given the constraints we can use 
        # the input array itself to mark the 
        # presence of numbers.
        for i in range(len(nums)):
            # For each number `num`, mark 
            # index `abs(num) - 1` as negative
            # to indicate that number exists.
            # Remember to take absolute value here!
            idx_to_mark = abs(nums[i]) - 1
            if nums[idx_to_mark] > 0:
                nums[idx_to_mark] *= -1

        res = []
        # In the second pass, any index that
        # remains positive corresponds to a missing
        # number. If negative number is found,
        # revert it to initial form to avoid
        # changing the original array.
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] *= -1
            else:
                # i + 1 is missing since nums[i] was never marked
                res.append(i + 1)
        return res
