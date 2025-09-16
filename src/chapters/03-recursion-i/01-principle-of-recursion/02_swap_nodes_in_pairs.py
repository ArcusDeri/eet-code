# https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1681/
# Definition for singly-linked list.
#  class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Intuition:
        # Separate a single "current" pair, swap
        # the nodes and attach the tail using recursion.
        if head is None or head.next is None:
            return head
        
        tail = self.swapPairs(head.next.next)
        newHead = head.next
        newHead.next = head
        head.next = tail
        return newHead
        