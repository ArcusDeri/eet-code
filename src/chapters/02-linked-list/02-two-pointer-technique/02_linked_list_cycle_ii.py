# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Idea: use slow and fast pointer to check
        # if there is a cycle at all. If found,
        # reset `fast` to starting node and move
        # both pointers by one until they meet again.
        # The second time they meet at the beginning
        # of the cycle (Floyd's Cycle Detection).
        if head is None:
            return None

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None
