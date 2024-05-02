from typing import List

class Solution:
    '''
    Split the array into positives and negatives
    Since we want to do lookup in the negatives, convert it to a set for faster operation
    Sort the positives in decreasing order and check for elemnts with their negatives in our -ve set
    The decreasing order sorting ensures the first element that fulfils our condition is the largest
    So return that element so we can exit early if possible
    '''
    def findMaxK(self, nums: List[int]) -> int:
        positives = sorted([x for x in nums if x > 0], reverse=True)
        negatives = set([x for x in nums if x < 0])
        
        for nums in positives:
            if (nums * -1) in negatives:
                return nums
        
        return -1


        