from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        '''
        DP solution with two choices: keep a pair or skip a pair
        Track longest valid chain in the process
        '''
        pairs = sorted(pairs, key=lambda x: x[0])
        cache = dict()

        def helper(i, prev):
            if i == len(pairs):
                return 0
            
            if (i, prev) in cache:
                return cache[(i, prev)]
            
            # Skip a pair
            res = helper(i + 1, prev)

            # Choose a pair
            if prev == None or pairs[prev][1] < pairs[i][0]:
                res = max(res, 1 + helper(i + 1, i))

            cache[(i, prev)] = res

            return res

        
        return helper(0, None)
        