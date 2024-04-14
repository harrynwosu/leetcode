# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        '''
        Perform dfs on the tree passing the parent and grandparent values along with each node ~down the tree
        '''
        self.sum = 0

        def dfs(node, parent = None, grandparent = None):
            if not node:
                return
            
            if grandparent and grandparent % 2 == 0:
                self.sum += node.val

            dfs(node.left, node.val, parent)
            dfs(node.right, node.val, parent)
        
        dfs(root)
        return self.sum
        