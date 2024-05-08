from typing import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        '''
        Add all the covered integers from the given ranges to a set
        For each number between left and right, check if it in our covered set
        All present, return True otherwise False
        '''
        covered = set()

        for start, end in ranges:
            for num in range(start, end+1):
                covered.add(num)
        
        for num in range(left, right+1):
            if num not in covered:
                return False
        
        return True

        
        