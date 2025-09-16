# https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/2384/
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def innerGenerateTrees(self, start, end):
        # Recursion condition - if "true" then it means
        # we are trying to generate subtrees where they
        # can't be expected. E.g. left subtree of node `1`
        # is always empty.
        if start > end:
            # It's tempting to return an empty list
            # but then we will skip elements in the loop below.
            # That's when one side subtree is empty - we still
            # want to iterate then so return None here.
            return [None]

        result = []
        # Generate trees where each number is the root node
        for n in range(start, end + 1):
            # Generate left subtrees
            for left in self.innerGenerateTrees(start, n - 1):
                # Generate right subtrees
                for right in self.innerGenerateTrees(n + 1, end):
                    result.append(TreeNode(n, left, right))
        return result
        

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        return self.innerGenerateTrees(1, n)
