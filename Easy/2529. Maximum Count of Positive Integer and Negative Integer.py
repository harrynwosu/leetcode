from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        '''
        Count the number of positives and negatives in the array and return the max
        '''
        pos, neg = 0, 0

        for i in range(len(nums)):
            if nums[i] < 0:
                neg += 1 
            elif nums[i] > 0:
                pos += 1
        
        return max(neg, pos)

        
        