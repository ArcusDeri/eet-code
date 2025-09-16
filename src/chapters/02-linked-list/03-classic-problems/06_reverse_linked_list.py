# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1205/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList1(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # iterative solution
        # Idea: build reversed list on the go
        # when iterating the nodes using helper
        # variables.
        newHead = None
        current = head
        while current is not None:
            temp = current
            current = current.next
            temp.next = newHead
            newHead = temp

        return newHead

    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # recursive solution
        if head is None or head.next is None:
            return head

        reversed = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversed
        
