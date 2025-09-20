# https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1139/
class ListNode(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyHashSet(object):
    # Intuition:
    # Naive hashing function combined with
    # linked list collision resolution.

    def __init__(self):
        self.table = [ListNode(None) for i in range(10 ** 3)]

    def get_hash(self, o):
        return o % len(self.table)

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash = self.get_hash(key)
        current = self.table[hash]
        while current.next:
            current = current.next
            if current.val == key:
                return
        current.next = ListNode(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash = self.get_hash(key)
        current = self.table[hash]
        while current.next and current.next.val != key:
            current = current.next
        if current.next:
            current.next = current.next.next

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        hash = self.get_hash(key)
        current = self.table[hash]
        while current:
            if current.val == key:
                return True
            current = current.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
