from typing import List

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        '''
        Use sets to keep track of valid numbers
        Can also be done using intersection and union like so:
        return list(set1 & set2 | set1 & set3 | set2 & set3)
        '''
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)

        res = set()

        for num in set1:
            if num in set2 or num in set3:
                res.add(num)
        
        for num in set2:
            if num in set1 or num in set3:
                res.add(num)
        
        for num in set3:
            if num in set1 or num in set2:
                res.add(num)
        
        return list(res)