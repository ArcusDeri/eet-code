# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1225/
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten_to_tail(self, head):
        # Intuition:
        # Use recursion - flatten child list if present.
        # This function returns the last node of the list
        # so that ew don't iterate the list twice (one time
        # to flatten, second time to connect last node of 
        # flattened child with detached `next`).
        current = head
        tail = head

        while current:
            if current.child:
                tail = self.flatten_to_tail(current.child)
                tail.next = current.next
                if tail.next:
                    tail.next.prev = tail
                current.next = current.child
                current.next.prev = current
                current.child = None
            else:
                tail = current
            current = current.next
        return tail


    def flatten(self,head):
        # Use a helper function for efficiency.
        self.flatten_to_tail(head)
        return head   