from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        '''
        For each student, check if the queryTime falls within the range of their howework times.
        If it does, add it to the count
        Return the count
        '''
        count = 0

        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1
        
        return count
        