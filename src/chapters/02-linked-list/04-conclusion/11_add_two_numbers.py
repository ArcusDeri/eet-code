# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1228/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Intuition:
        # Iterate both lists. If both point to values,
        # perform addition while remembering about `carry`.
        # Follow up with remaining nodes.

        dummy = ListNode()
        current = dummy
        l1Ptr, l2Ptr = l1, l2
        carry = 0
        while l1Ptr and l2Ptr:
            v = l1Ptr.val + l2Ptr.val + carry
            carry = v // 10
            v %= 10
            current.next = ListNode(v)
            current = current.next
            l1Ptr = l1Ptr.next
            l2Ptr = l2Ptr.next

        remaining = l1Ptr if l1Ptr else l2Ptr
        while remaining:
            v = remaining.val + carry
            carry = v // 10
            v %= 10
            current.next = ListNode(v)
            current = current.next
            remaining = remaining.next
        
        # Handle cases like "7 + 3" - no pointers are valid
        # but there is still a value we need to carry over.
        if carry > 0:
            current.next = ListNode(carry)
        
        return dummy.next
