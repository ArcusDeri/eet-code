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
