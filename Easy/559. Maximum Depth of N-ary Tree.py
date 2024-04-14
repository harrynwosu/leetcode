class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node) -> int:
        '''
        Reference: 104. Maximum depth of Binary Tree. (Similar Logic)
        Add 1 to the max_depth so far on each step as we go deeper into the tree
        To handle cases where node.children is empty (a leaf), return 1 and exit so as not to encounter error on `max([dfs(child) for child in node.children])`
        '''
        def dfs(node):
            if not node:
                return 0

            if not node.children:
                return 1
            
            return 1 + max([dfs(child) for child in node.children])
        
        return dfs(root)
    
