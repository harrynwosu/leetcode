from collections import defaultdict, deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        Build adjacency list for nodes
        Continuously remove all leaves of the graph/tree (nodes with a single edge/neighbor) until we have only 1 or 2 nodes left
        The node(s) left are the roots of the MHTs of the graph
        '''
        if n == 1:
            return [0]

        graph = defaultdict(list)

        # Build adjacency list
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        num_edges = dict()
        for node in graph:
            num_edges[node] = len(graph[node])
         
        leaves = deque([node for node in num_edges if num_edges[node] == 1])

        # Continuously remove all leaves until only one or two nodes left
        while leaves:
            if len(num_edges) <= 2:
                break

            for _ in range(len(leaves)):
                curr_node = leaves.popleft()
                del num_edges[curr_node]

                for neighbor in graph[curr_node]:
                    # Since graph is unirected, deleted leaves could still be neighbors of remaining nodes so check if it still has edges
                    if neighbor in num_edges:
                        num_edges[neighbor] -= 1
                        if num_edges[neighbor] == 1:
                            leaves.append(neighbor)
        
        return list(num_edges.keys())
    
    def findMinHeightTrees2(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        Time Limit Exceeded
        Build adjacency list for nodes
        For each node, run bfs and get its height
        Store the heights of each node in a hasmap
        Get nodes with minimum height
        '''
        if n == 1:
            return [0]

        res = []
        # min_height = float("inf")
        heights = dict()
        graph = defaultdict(list)

        # Build adjacency list
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        for node in graph:
            q = deque([node])
            visited = set()
            height = 0

            while q:
                if len(visited) == len(graph.keys()):
                    break
                
                level_count = len(q)
                    
                for _ in range(level_count):
                    curr = q.popleft()

                    if curr not in visited:
                        q += graph[curr]
                        visited.add(curr)
                    
                height += 1
                
            heights[node] = height
            
        min_height = min(heights.values())
        for node, h in heights.items():
            if h == min_height:
                res.append(node)

        return res

        
        