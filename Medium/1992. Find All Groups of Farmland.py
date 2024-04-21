class Solution:
    def findFarmland(self, land):
        '''
        Reference: 200. Number of Islands
        Use dfs to find all individual sets of farmland groups, while keeping track of the current top left and bottom right cell
        The top left corner of each group will have the smallest x and y co-ordinates while bottom right has the largest
        Loop through each element in the grid checking if it is a farmland (== 1) or already part of an existing farmland (in visited)
        If it is a new farmland group, intitialize the top left and bottom right cell to that cell, then find all adjacent lands with our dfs.
        The dfs function update the top left and bottom right if necessary.
        After all adjacent lands have been found (dfs from that cell complete), add the final top left and bottom right coordinates of that group to final result array.
        '''
        m, n = len(land), len(land[0])
        visited = set()
        res = []

        def in_bounds(row, col):
            return (0 <= row < m) and (0 <= col < n)

        def dfs(row, col):
            nonlocal top_left, bottom_right
            directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
            for x, y in directions:
                new_row, new_col = row+x, col+y
                if in_bounds(new_row, new_col) and (new_row, new_col) not in visited and land[new_row][new_col] == 1:
                    visited.add((new_row, new_col))
                    if new_row <= top_left[0] and new_col <= top_left[1]:
                        top_left = (new_row, new_col)
                    elif new_row >= bottom_right[0] and new_col >= bottom_right[1]:
                        bottom_right = (new_row, new_col)
                    dfs(new_row, new_col)

        
        for row in range(m):
            for col in range(n):
                if land[row][col] == 1 and (row, col) not in visited:
                    top_left = (row, col)
                    bottom_right = (row, col)
                    dfs(row, col)
                    res.append([top_left[0], top_left[1], bottom_right[0], bottom_right[1]])
        
        return res


        