# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode | None, val: int, depth: int) -> TreeNode | None:
        '''
        Perform dfs on the tree, keeping track of the current depth we are at in the tree
        When we reach the node whose children need to be changec (depth -1), store the current left and right nodes of that node in variables left and right
        Create 2 nodes with value, val and make them the new left and right children of the current node
        Make the original left subtree of the current the left subtree of the new node
        Make the original right subtree of the current the right subtree of the new node
        Return once the change has been made as we don't need to go deeper in the tree after that node.
        Keep going deeper if we haven't reached the node whose children need to be changed yet by recursively calling dfs.
        If the change involves creating a new root (depth = 1), do that and don't call dfs on the tree
        '''
        def dfs(node, d):
            if not node:
                return
            if d == depth - 1:
                left = node.left
                right = node.right

                node.left = TreeNode(val)
                node.left.left = left

                node.right = TreeNode(val)
                node.right.right = right
                return
            
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)

        if depth == 1:
            old_root = root
            root = TreeNode(val)
            root.left = old_root
        else:
            dfs(root, 1)

        return root