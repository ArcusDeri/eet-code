# https://leetcode.com/explore/learn/card/linked-list/210/doubly-linked-list/1294/

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

class Node(object):
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList(object):
    def __init__(self):
        self.head = None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        current = self.head
        i = 0
        while i < index:
            if current is None:
                return -1
            current = current.next
            i += 1
        return current.val if current else -1
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        n = Node(val, self.head)
        self.head = n
        if self.head.next:
            self.head.next.prev = self.head
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        n = Node(val)
        if self.head is None:
            self.head = n
            return
        current = self.head
        while current and current.next:
            current = current.next
        current.next = n
        n.prev = current
        

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
        current = self.head
        while i < index:
            if current is None:
                return
            current = current.next
            i += 1
        if current is None:
            return
        current.next = Node(val, current.next)
        if current.next.next:
            current.next.next.prev = current.next
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if self.head is None:
            return
        if index == 0:
            tmp = self.head
            self.head = self.head.next
            tmp.next = None
            return
        i = 1
        current = self.head
        while i < index:
            if current is None:
                return
            current = current.next
            i += 1
        if current is None or current.next is None:
            return

        tmp = current.next.next
        current.next.next = None
        current.next = tmp
        if tmp:
            tmp.prev = current
