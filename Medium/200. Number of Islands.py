from collections import deque

class Solution:
    def numIslands(self, grid) -> int:
        '''
        Use bfs/dfs to add all adjacent 1s (islands) to visited set
        Loop through each element in the grid checking if it is land (== "1") 
        or already part of an existing island (in visited)
        If conditions met to be a fresh island , find all adjacent lands.
        Increment # of islands after this bfs/dfs
        '''
        m, n = len(grid), len(grid[0])

        visited = set()

        def in_bounds(row, col):
            return (0 <= row < m) and (0 <= col < n)

        def bfs(i, j):
            q = deque()
            q.append((i, j))
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            while q: 
                row, col = q.popleft()
                for x, y in directions:
                    if in_bounds(row+x, col+y) and grid[row+x][col+y] == "1" and (row+x, col+y) not in visited:
                        visited.add((row+x, col+y))
                        q.append((row+x, col+y))

        def dfs(row, col):
            directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
            visited.add((row, col))
            for x, y in directions:
                new_row, new_col = row+x, col+y
                if (new_row, new_col) not in visited and in_bounds(new_row, new_col)and grid[new_row][new_col] == "1":
                    dfs(new_row, new_col)
                    

        islands = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        
        return islands


        