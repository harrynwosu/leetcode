from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        Use two pointers on the sorted array
        Prioritize matching larger weights (at end) to smallest possible weight
        If the two are less than limit, they can fit a boat
        Else, the large weight can't fit with no one else so has a single boat
        '''
        people.sort()
        count = 0
        i, j = 0, len(people) - 1

        while i <= j:
            curr_total = people[i] + people[j]
            if curr_total <= limit:
                i += 1
                
            j -= 1
            count += 1
                
        return count

        