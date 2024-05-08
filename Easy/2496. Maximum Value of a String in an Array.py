from typing import List

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        '''
        Convert each element to it's corresponding value inplace based on if the string is completely numeric or not
        Return the maximum value in the array
        '''
        for i in range(len(strs)):
            strs[i] = int(strs[i]) if strs[i].isnumeric() else len(strs[i]) 
        
        return max(strs)

        