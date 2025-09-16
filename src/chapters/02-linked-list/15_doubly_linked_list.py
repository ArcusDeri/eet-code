# https://leetcode.com/explore/learn/card/linked-list/210/doubly-linked-list/1294/

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

class MyNode(object):
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        i = 0
        current = self.head
        while i <= index and current:
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
        n = MyNode(val)
        n.next = self.head
        if self.head:
            self.head.prev = n
        self.head = n

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.head:
            self.head = MyNode(val)
            return
        current = self.head
        while current and current.next:
            current = current.next
        if current:
            n = MyNode(val)
            current.next = n
            n.prev = current
        
    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        i = 0
        current = self.head
        if index == 0:
            self.addAtHead(val)
            return
        while current:
            if i + 1 == index:
                n = MyNode(val)
                n.next = current.next
                if n.next: # Might be `None` because we have just updated `n.next``
                    n.next.prev = n
                current.next = n
            i += 1
            current = current.next

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if self.head is None:
            return

        if index == 0:
            n = self.head.next
            self.head.next = None
            self.head = n
            if n:
                n.prev = None
            return
        i = 0
        current = self.head
        while current:
            if i == index:
                # Index is larger than list length.
                break
            if i + 1 == index:
                if current.next:
                    current.next.prev = None
                    current.next = current.next.next
                if current.next:
                    current.next.prev = current
            i += 1
            current = current.next  
        