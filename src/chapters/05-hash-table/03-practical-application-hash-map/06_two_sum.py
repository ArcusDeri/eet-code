# https://leetcode.com/problems/two-sum/submissions/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Intuition:
        # Use heelper hash map where key is a number
        # from `nums` and value is its index in the array.
        # Iterate `nums` while checking if `seen`
        # contains the other number needed to reach the target.
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                # Hash map has the other number so we can
                # take its index from the map and concat it with
                # current index to return the result.
                return [i, seen[target - nums[i]]]
            # Save current number
            seen[nums[i]] = i
        # Execution should not reach here because exactly
        # one matching pair is guaranteed to be present in 
        # the array.
