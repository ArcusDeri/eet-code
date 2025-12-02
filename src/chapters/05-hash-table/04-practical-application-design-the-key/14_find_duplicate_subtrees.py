# https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1127/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[Optional[TreeNode]]
        """
        # Intuition:
        # serialize each node with their children. Store
        # serialized nodes in a dictionary. Append node
        # to result collection if already seen in the map.
        subtrees = {}
        res = []

        def dfs(node):
            if node is None:
                return 'n'
            
            left = dfs(node.left)
            right = dfs(node.right)
            k = ','.join([str(node.val), left, right])

            if k not in subtrees:
                subtrees[k] = [node]
            elif k in subtrees and len(subtrees[k]) == 1:
                res.append(subtrees[k][0])
                subtrees[k].append(node)
            else:
                subtrees[k].append(node)
            return k

        dfs(root)
        return res
