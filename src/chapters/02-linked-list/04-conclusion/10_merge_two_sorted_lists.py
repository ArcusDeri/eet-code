# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1227/
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Intuition: build the result list iteratively using
        # dummy head for convenience. Compare values if both
        # pointers are not null, otherwise append the rest.
        dummyHead = ListNode()
        res = dummyHead
        left = list1
        right = list2
        while left and right:
            if left.val < right.val:
                res.next = left
                left = left.next
            else:
                res.next = right
                right = right.next
            res = res.next
        
        if left:
            res.next = left
        elif right:
            res.next = right
        
        return dummyHead.next
