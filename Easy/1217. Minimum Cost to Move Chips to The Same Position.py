from typing import List

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        '''
        We can bring all the odd positioned coins at one odd place at cost 0
        Similarly, we can bring all the even positioned coins at one even place at cost 0.
    After this, we just need to find whether we place coins at the odd position to the even position or evens to odd position at, which will be the minimum cost at min( odd, even);
        '''
        odd_count = sum(pos % 2 for pos in position)
        even_count = sum(pos % 2 == 0 for pos in position)

        return min(odd_count, even_count)
        