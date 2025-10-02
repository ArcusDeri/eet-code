# https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1153/
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Intuition:
        # Use two pointers on opposite ends.
        # Spin until the sum equals the target.
        # If the sum is lower than the target,
        # increment `l`. Increment `r` otherwise.
        l, r = 0, len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        # Description says the array is 1-indexed so add 1.
        return [l + 1, r + 1]
