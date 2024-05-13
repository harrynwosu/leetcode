from typing import List

class Solution:
    '''
    Use prefix sums to keep track of the left sums and right sums at each element's position.
    '''
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        left_sum = 0

        right_sum = sum(nums)
        
        for i in range(len(nums)):
            right_sum -= nums[i]
            res[i] = abs(left_sum-right_sum)
            left_sum += nums[i]

        return res