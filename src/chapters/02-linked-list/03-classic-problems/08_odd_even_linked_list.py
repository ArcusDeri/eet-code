# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1208/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None

        # Intuition:
        # Build the result as two lists and connect
        # them before returning.
        evenHead = head.next
        currentOdd = head
        currentEven = head.next
        while currentEven and currentEven.next:
            currentOdd.next = currentEven.next
            currentOdd = currentOdd.next
            currentEven.next = currentOdd.next
            currentEven = currentEven.next
        
        currentOdd.next = evenHead
        return head
        