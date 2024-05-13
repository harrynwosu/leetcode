from typing import List

class Solution:
    '''
    Here we want to maximize two things:
        1. The individual binary numbers in the rows
        2. The number of 1s in each column
    This ensures that we have the maximum possible sum
    '''
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # If row starts with 0 flip the row to maximize that row
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 if grid[i][j] == 0 else 0
        
        # If a column has more 0s than 1s, flip it
        for j in range(n):
            zeros_count = [grid[i][j] for i in range(m)].count(0)
            if zeros_count > m - zeros_count:
                for i in range(m):
                    grid[i][j] = 1 if grid[i][j] == 0 else 0
        
        total = 0
        for i in range(m):
            bin_str = "".join([str(num) for num in grid[i]])
            total += int(bin_str, 2)
        
        return total