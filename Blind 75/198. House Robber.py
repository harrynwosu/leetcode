from functools import lru_cache
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        DP problem with two choices: skip current house or rob current house
        We need to return the maximum of the two
        '''
        @lru_cache(maxsize=None)
        def dp(i):
            if i >= len(nums):
                return 0
            
            res = max(
                nums[i] + dp(i + 2),  # rob current
                dp(i + 1)             # skip current
            )

            return res

        return dp(0)



        
        