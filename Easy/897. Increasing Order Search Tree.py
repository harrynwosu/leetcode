# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        '''
        Important: Inorder traversal always traverses a BST with its values in sorted order
        Perform inorder traversal and store the sorted values in an array
        Go through the array and act like creating a linked list
        Setting the curr.right to the values in the array
        '''
        self.tree = []

        def inorder(node):
            if not node:
                return 

            inorder(node.left)
            self.tree.append(node.val)
            inorder(node.right)

        inorder(root)

        curr = res =  TreeNode(self.tree[0])

        for val in self.tree[1:]:
            curr.right = TreeNode(val)
            curr = curr.right

        return res