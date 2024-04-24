from typing import List

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        '''
        Use set to store seen sums
        '''
        sums = set()

        for i in range(1, len(nums)):
            curr_sum = nums[i-1] + nums[i]
            if curr_sum in sums:
                return True
            sums.add(curr_sum)

        return False            
        