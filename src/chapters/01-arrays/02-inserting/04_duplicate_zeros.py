# https://leetcode.com/problems/duplicate-zeros/description/
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        zerosToDuplicateCount = 0
        length = len(arr) - 1
        i = 0

        # Count the zeros that will be duplicated,
        # then shift the elements to the right while
        # duplicating zeros if zero is being shifted.
        while i <= length - zerosToDuplicateCount:
            if arr[i] == 0:
                if i == length - zerosToDuplicateCount:
                    # Edge case. For example consider:
                    # [1, 0, 2, 0, 3] -> [1, 0, 0, 2, 0]
                    # Notice how the second zero isn't duplicated
                    # because the duplicate would land out of bounds.
                    # For edge case set last element to 0 and decrease
                    # `length` by one so that we don't modify this element
                    # in the second loop.
                    arr[length] = 0
                    length -= 1
                    # Leave the loop so the zero counter doesn't increase.
                    # We don't want to duplicate this zero, it is handled
                    # above.
                    break
                zerosToDuplicateCount += 1
            i += 1

        i = length - zerosToDuplicateCount
        while zerosToDuplicateCount > 0:
            # Shift current element by the number of zeros left
            arr[i + zerosToDuplicateCount] = arr[i] 
            if arr[i] == 0:
                # Duplicate zero
                zerosToDuplicateCount -= 1
                arr[i + zerosToDuplicateCount] = 0
            i -= 1
