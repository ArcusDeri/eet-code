# https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/2378/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Intuition:
        # Reverse the tail and attach haed to the end
        # leveraging how the nodes are connected after
        # reversal: `head.next` points to the very last
        # node in the reversed tail.w
        if head is None or head.next is None:
            return head
        reversed = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversed

