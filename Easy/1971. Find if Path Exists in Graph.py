from collections import deque, defaultdict

class Solution:
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        '''
        Build the graph adjacency list
        Use bfs to search for path. Add the source to the queue
        For each node in the queue, if it is equal to destination, return True
        Else if the node hasn't been visited, add all its neighbors to the queue
        Continue until the queue is empty
        '''
        graph = defaultdict(list)

        # Build adjacency list
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])  # Bi-diredctional

        visited = set()
        q = deque()
        q.append(source)

        while q:
            curr = q.popleft()
            if curr == destination:
                    return True
            elif curr not in visited:
                    q += graph[curr]
                    visited.add(curr)
        
        return False




        


        