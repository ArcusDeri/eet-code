# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ptrA = headA
        ptrB = headB
        # General idea is to use a little trick:
        # we need to "align" both pointers and this can
        # be achieved if we simply switch to the other
        # side when the end is reached.
        while ptrA or ptrB:
            if ptrA is ptrB:
                return ptrA

            if ptrA is None:
                ptrA = headB
            else:
                ptrA = ptrA.next

            if ptrB is None:
                ptrB = headA
            else:
                ptrB = ptrB.next
        return None
