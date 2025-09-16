# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        current = head

        while current and current.next:
            if current.next.val is val:
                current.next = current.next.next
            else:
                current = current.next

        # Remember that first node might be the one that should be
        # also removed.
        return head.next if head and head.val is val else head
