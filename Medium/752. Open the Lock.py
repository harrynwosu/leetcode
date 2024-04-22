from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        '''
        BFS: Graph Traversal
        Handle each combination like a node
        Each node's neighbors will be every single combination that can be made in one move from that node
        Once we reach target, return how deep we are in the dfs
        '''
        visited, invalid = set(), set(deadends)
        q = deque(["0000"])
        level = 0

        while q:
            level_count = len(q)

            for i in range(level_count):
                curr = q.popleft()

                if curr == target:
                    return level
                
                if curr in visited or curr in invalid:
                    continue
                
                visited.add(curr)

                # For each wheel
                for i in range(4):
                    curr_slot = int(curr[i])
                    forward_turn = str((curr_slot + 1) % 10)
                    backward_turn = str((curr_slot - 1) % 10)
                    q.append((curr[0:i] + forward_turn + curr[i+1:]))
                    q.append((curr[0:i] + backward_turn + curr[i+1:]))

            level += 1
                
        return -1

                


