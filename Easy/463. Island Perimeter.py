class Solution:
    def islandPerimeter(self, grid) -> int:
        '''
        Each cell has 4 sides and each of these 4 sides is added to the overall perimeter only if that side is not connected to a neighbor.
        So to solve this, for each land cell, count how many other land neighbors are around it in all 4 directions (up, right, down, left).
        Be sure to check that cells are in bounds of the grid when checking in all 4 directions of a land cell 
        Subtract this count from 4 and add it to the global perimeter
        '''
        m, n = len(grid), len(grid[0])
        perimeter = 0

        def in_bounds(row, col):
            return (0 <= row < m) and (0 <= col < n) 

        def count_land_neighbors(row, col):
            count = 0
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for x, y in directions:
                if in_bounds(row+x, col+y) and grid[row+x][col+y] == 1:
                    count += 1
            
            return count
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    perimeter += (4 - count_land_neighbors(row, col))
        
        return perimeter

                

        