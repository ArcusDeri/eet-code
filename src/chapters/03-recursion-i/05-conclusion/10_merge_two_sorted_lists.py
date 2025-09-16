# https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/2382/
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
        if list1 and list2:
            if list1.val < list2.val:
                tail = self.mergeTwoLists(list1.next, list2)
                list1.next = tail
                return list1
            else:
                tail = self.mergeTwoLists(list1, list2.next)
                list2.next = tail
                return list2
        if list1:
            return list1
        else:
            return list2


        
