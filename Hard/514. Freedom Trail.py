from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        '''
        DP problem that involves two choices: going forward (clockwise) or backwards (anti-clockwise) for every occurence of the matching character in ring
        Calculate minimum cost to each occurrence of the current char in key we are looking for
        '''
        ring_len = len(ring)
        key_len = len(key)
        
        @lru_cache(maxsize=None)
        def helper(key_idx, ring_idx):
            # ring_idx: idx of current position in ring
            if key_idx == key_len: # All key characters found
                return 0
            
            res = float("inf")
            for idx, char in enumerate(ring):
                # idx: current ring index during loop
                if char == key[key_idx]:
                    # Calculate min distance from 
                    min_distance = min (
                        abs(idx - ring_idx),            # clockwise
                        ring_len - abs(idx - ring_idx)  # counter-clockwise
                    )
                    # To check if a previously computed distance in the loop is less than the current dist
                    res = min (
                        res,
                        1 + min_distance + helper(key_idx + 1, idx)
                    )
            
            return res
            

        return helper(0, 0)
            


            