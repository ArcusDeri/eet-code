# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1229/
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # Intuition:
        # Build a mapping of original nodes to clones.
        # Then use the mapping to set random nodes in the
        # cloned linked list.
        # Alternatively:
        # Iterate the list three times:
        # 1. clone each node
        # 2. assign random nodes for cloned nodes
        # 3. separate original and cloned nodes
        mapping = {}
        currentOriginal = head
        dummyHead = Node(0)
        currentNew = dummyHead

        # Shallow clone and build a mapping
        while currentOriginal:
            nextNew = Node(currentOriginal.val)
            mapping[currentOriginal] = nextNew
            currentNew.next = nextNew
            currentNew = currentNew.next
            currentOriginal = currentOriginal.next
        
        # Go over the list again this time cloning random
        # nodes using the mapping
        currentOriginal = head
        currentNew = dummyHead.next
        while currentOriginal:
            if currentOriginal.random:
                currentNew.random = mapping[currentOriginal.random]
            currentOriginal = currentOriginal.next
            currentNew = currentNew.next
        
        return dummyHead.next

    def copyRandomListAlt(self, head):
            """
            :type head: Node
            :rtype: Node
            """
            if head is None:
                return None
            c = head
            while c:
                t = c.next
                c.next = Node(c.val)
                c.next.next = t
                c = c.next.next
            c = head
            while c and c.next:
                if c.random:
                    c.next.random = c.random.next
                c = c.next.next
            c = head
            cc = head.next
            res = head.next
            while c and c.next:
                c.next = c.next.next
                if cc.next:
                    cc.next = cc.next.next
                c = c.next
                cc = cc.next
            return res
