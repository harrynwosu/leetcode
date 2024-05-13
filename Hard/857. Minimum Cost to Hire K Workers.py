import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        '''
        All workers in a group should have the same wage-quality ratio for them to meet the criteria.
        Wage for
        '''
        # Sort workers by the wage-quality ratio, to make sure we have an always consider smaller ratios before larger ones during the loop. This will ensure that once we are examining a current worker, every other one that came before it has a lower ratio so those will need to be at most increased to match the current
        workers = sorted([(w, q) for w, q in zip(wage, quality)], key=lambda x: x[0] / x[1])

        total_quality, min_cost = 0, float("inf")
        max_heap = []   # Keep track of our current group

        for wage, quality in workers:
            total_quality += quality

            heapq.heappush(max_heap, -quality)

            # If we exceed the expected group size, remove the current largest quality in the group (from the heap and total quality)
            if len(max_heap) > k:   
                # Since we store quality as negtives (for max_heap), adding subtracts it from total_quality
                total_quality += heapq.heappop(max_heap)
            
            if len(max_heap) == k:
                min_cost = min(min_cost, (wage / quality) * total_quality)
        

        return min_cost