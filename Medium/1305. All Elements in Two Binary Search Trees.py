# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode):
        '''
        Important: Inorder traversal always traverses a BST with its values in sorted order
        Approach 1: 
            1. Use inorder traversal to traverse the two BSTs in sorted order into two different arrays
            2. Use two pinters to merge the two sorted arrays
        '''
        tree1, tree2 = [], []

        def dfs(node, arr):
            if not node:
                return

            dfs(node.left, arr)
            arr.append(node.val)
            dfs(node.right, arr)
        
        dfs(root1, tree1)
        dfs(root2, tree2)

        i, j = 0, 0
        res = []

        while i < len(tree1) and j < len(tree2):
            if tree1[i] <= tree2[j]:
                res.append(tree1[i])
                i += 1
            else:
                res.append(tree2[j])
                j +=1

        while i < len(tree1):
            res.append(tree1[i])
            i += 1
        
        while j < len(tree2):
            res.append(tree2[j])
            j += 1
        
        return res

    '''
    Approach 2: Traverse the two trees into one array and sort
    '''
    def getAllElements2(self, root1: TreeNode, root2: TreeNode):
        self.res = []

        def dfs(node):
            if not node:
                return

            self.res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root1)
        dfs(root2)

        return sorted(self.res)
            

        