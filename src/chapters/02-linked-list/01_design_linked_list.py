# https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/
class MyNode(object):
    def __init__(self, val):
        self.value = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if self.head == None:
            return -1
        i = 0
        current = self.head
        while current != None:
            if i == index:
                return current.value
            current = current.next
            i += 1
        return -1
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        newHead = MyNode(val)
        newHead.next = self.head
        self.head = newHead
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head is None:
            self.head = MyNode(val)
            return

        current = self.head
        while current != None and current.next != None:
            current = current.next
        
        newTail = MyNode(val)
        current.next = newTail
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        current = self.head
        i = 0

        if index == 0:
            self.addAtHead(val)
            return

        while current != None:
            if i == index - 1:
                node = MyNode(val)
                node.next = current.next
                current.next = node
                return
            i += 1
            current = current.next

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if self.head is None:
            return

        if index is 0:
            self.head = self.head.next
            return

        current = self.head
        i = 0
        while current is not None and current.next is not None:
            if i == index - 1:
                current.next = current.next.next
                return
            i += 1
            current = current.next
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
