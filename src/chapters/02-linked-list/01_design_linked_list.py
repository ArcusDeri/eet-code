# https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/
class Node(object):
    def __init__(self, v, n = None):
        self.val = v
        self.next = n

class MyLinkedList(object):
    def __init__(self):
        self.head = None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        c = self.head
        i = 0
        while c:
            if i == index:
                return c.val
            elif i > index:
                return -1
            c = c.next
            i += 1
        return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.head = Node(val, self.head)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        c = self.head
        while c and c.next:
            c = c.next
        if c:
            c.next = Node(val)
        else:
            self.head = Node(val)
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0:
            self.addAtHead(val)
            return
        i = 1
        c = self.head
        while c and c.next:
            if i == index:
                c.next = Node(val, c.next)
                return
            i += 1
            c = c.next
        if not c:
            return
        if i == index:
            c.next = Node(val, c.next)

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index == 0 and self.head:
            self.head = self.head.next
            return
        i = 1
        c = self.head
        while c and c.next:
            if i == index:
                c.next = c.next.next
                return
            i += 1
            c = c.next
