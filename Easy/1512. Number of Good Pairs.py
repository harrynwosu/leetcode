from collections import defaultdict
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = defaultdict(list)
        count = 0

        for idx, num in enumerate(nums):
            if num in pairs:
                count += len(pairs[num])
            pairs[num].append(idx)
        
        return count