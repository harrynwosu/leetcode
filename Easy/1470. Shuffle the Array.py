from typing import List

class Solution:
    '''
    Use two pointers, i from start and j from middle
    Alternatively add the element at each pointer to the result array and increment the pointers 
    to get ready for the next set of elements
    '''
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        j = len(nums) // 2

        for i in range(j):
            res.append(nums[i])
            res.append(nums[j])
            j += 1
        
        return res
        