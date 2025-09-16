# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1209/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverse(self, head):
        newHead = None
        current = head
        while current:
            temp = current.next
            current.next = newHead
            newHead = current
            current = temp
        return newHead

    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True

        # Intuition:
        # Use `slow` and `fast` pointers to find the middle of the
        # list. Reverse one half and compare values node by node with
        # the other half. Remember to reverse back the list so it 
        # stays the same.
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        secondHalfStart = self.reverse(slow)
        secondHalfPtr = secondHalfStart

        # Now compare if first half is the same as the other.
        slow = head
        result = True
        while result and secondHalfPtr:
            if slow.val is not secondHalfPtr.val:
                result = False
                break
            slow = slow.next
            secondHalfPtr = secondHalfPtr.next

        # Reverse back the second half
        self.reverse(secondHalfStart)
        return result
