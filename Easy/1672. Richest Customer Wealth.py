from typing import List

class Solution:
    '''
    Keep track of max sum for each customer and return final max
    '''
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0

        for customer in accounts:
            max_wealth = max(max_wealth, sum(customer))

        return max_wealth
        