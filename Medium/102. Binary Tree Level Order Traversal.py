from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Standard BFS
        '''
        if not root:
            return []
            
        q = deque([root])
        res = []
        
        while q:
            level_count = len(q)
            level = []

            for _ in range(level_count):
                curr = q.popleft()
                level.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
            
            res.append(level)
        
        return res
            
        