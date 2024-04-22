from typing import Optional, List
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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

                for node in curr.children:
                    if node:
                        q.append(node)
            
            res.append(level)
        
        return res
        