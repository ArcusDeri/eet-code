# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Idea: use `left` and `right` pointers. First iterate `right`
        # by `n`. Then iterate `right` until `right.next` is None while
        # iterating `left` from the beginning at the same time. This way
        # the node to be deleted can be found in one go.
        
        # Handle edge case.
        if head.next is None and n is 1:
            return None
        
        i = 0
        right = head
        while i < n:
            right = right.next
            i += 1

        left = head
        if right is None:
            # Edge case - we have to remove the very first node
            return head.next

        while right.next is not None:
            right = right.next
            left = left.next
        
        left.next = left.next.next
        return head
