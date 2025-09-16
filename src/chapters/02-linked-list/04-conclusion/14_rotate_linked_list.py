# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1295/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Intuition:
        # Connect the last node with the head and find
        # length of the list to "correct" `k` if it's
        # greater than the length. Then iterate from the
        # start until `i` is equal to `length - k` and 
        # "cut" the list. The next node is the result.
        if head is None or head.next is None or k is 0:
            return head

        # Start at 1 - the condition above is not satisfied
        # so we have at least one node. By starting at 1
        # we will discover the length while still pointing
        # at a valid node instad of at None.
        listLen = 1
        current = head
        while current.next:
            listLen += 1
            current = current.next
        
        # Handle k > listLen.
        k = k % listLen
        # Return early if possible.
        if k is 0:
            return head
        
        # Connect end with start.
        current.next = head

        # Node that will be the last in the rotated list.
        i = 1
        current = head
        while i < listLen - k:
            current = current.next
            i += 1
        
        result = current.next
        current.next = None
        return result