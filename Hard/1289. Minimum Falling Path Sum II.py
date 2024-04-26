from typing import List
from functools import lru_cache

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        '''
        DP problem where our choices are the different paths to take (in this case different paths are all the cells in the next row below current cell except the one directly below it)
        Explore all these valid paths to take and track the minimum sum generated
        Here, lru_cache is faster than 2D dp array which is faster than hashmap cache
        '''
        m, n = len(grid), len(grid[0])
        # cache = dict()
        # dp = [[None] * n for _ in range(m)]

        def in_bounds(row):
            # Ensure that we don't add columns that don't exist
            return 0 <= row < m
        
        @lru_cache(maxsize=None)
        def helper(row, col):   # (row, col)
            if not in_bounds(row + 1):
                return grid[row][col]

            # if (row, col) in cache:
            #     return cache[row, col]

            # if dp[row][col]:
            #     return dp[row][col]

            minimum = float("inf")
            for c in range(n):
                if c != col:
                    minimum = min(minimum, helper(row + 1, c))
    
            # cache[(row, col)] = grid[row][col] + minimum
            # dp[row][col] = grid[row][col] + minimum

            return grid[row][col] + minimum


            # return cache[(row, col)]
            # return dp[row][col]
            
        min_path_sum = float("inf")
        for j in range(n):
            min_path_sum = min(min_path_sum, helper(0, j))
            
        return min_path_sum
        