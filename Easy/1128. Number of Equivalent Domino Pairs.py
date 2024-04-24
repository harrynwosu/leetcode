from typing import List
from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """
        Use a hashmap to check for past occurences of a domino or its reverse in the list and increment count accordingly
        Edge case: When checking for reverses, be careful to avoid the case when the two umbers are the same so its reverse is essentially the same domino
        """
        pair_count = defaultdict(int)
        count = 0

        for domino in dominoes:
            if (domino[0], domino[1]) in pair_count:
                count += pair_count[(domino[0], domino[1])]
            if (domino[1], domino[0]) in pair_count and domino[1] != domino[0]:
                count += pair_count[(domino[1], domino[0])]

            pair_count[(domino[0], domino[1])] += 1
        
        return count


        