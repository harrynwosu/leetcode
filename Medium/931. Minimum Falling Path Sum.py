from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        '''
        DP problem where our choices are the different paths to take
        Explore all valid paths to take and track the minimum sum
        '''
        m, n = len(matrix), len(matrix[0])

        cache = dict()
        
        def in_bounds(row, col):
            # Ensure that we don't add columns that don't exist
            return 0 <= col < m
        
        # We can use this in place of manually handling the cache
        # @lru_cache(maxsize=None)
        def helper(row, col):   # (row, col)
            # Invalidate invalid cells by making them as large as possible so they are never returned with min()
            if not in_bounds(row, col):
                return float("inf")

            if row == m:
                return 0

            if (row,col) in cache:
                return cache[(row, col)]
            
            res =  matrix[row][col] + min(
                            helper(row + 1, col - 1),
                            helper(row + 1, col),
                            helper(row + 1, col + 1)
                        )
            
            cache[(row, col)] = res
            return res

        min_sum = float("inf")
        for j in range(n):
            min_sum = min(min_sum, helper(0, j))
        
        return min_sum