# https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1140/
class ListNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap(object):
    # Intuition:
    # Like in Hashset, use linked list for
    # collision resolution. Each node has
    # key, value and next properties.
    def __init__(self):
        self.table = [ ListNode(None, None) for _ in range(10 ** 4)]

    def get_hash(self, o):
        return o % len(self.table)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        current = self.table[self.get_hash(key)]
        while current.next:
            current = current.next
            if current.key == key:
                current.val = value
                return
        current.next = ListNode(key, value)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        current = self.table[self.get_hash(key)]
        while current.next:
            current = current.next
            if current.key == key:
                return current.val
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        current = self.table[self.get_hash(key)]
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
