# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        '''
        A tree that returns -1 here is unbalanced
        Return -1 if unbalanced, else return depth of tree
        Any child tree that is unbalanced makes all the ancestors unbalanced so just move the -1 up the tree from that node.
        '''

        def dfs(node):
            if not node:
                return 0 

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            if left_depth == -1 or right_depth == -1:
                return -1
            
            if abs(left_depth - right_depth) > 1:
                return -1


            return 1 + max(left_depth, right_depth)


        return dfs(root) != -1
        