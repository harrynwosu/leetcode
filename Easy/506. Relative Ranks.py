import heapq
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        '''
        Use a max heap to store the scores and their indices in descending order
        Keep track of the current rank of the athletes, and a new array for the result with the same length as the score arr
        Loop through the max heap: Pop from the max_heap; if the rank is between 1-3, replace the same index of that athlete in the new array with the corresponding medal, else replace the index with the string representation of the rank
        '''
        winners = { 1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal" }
        max_heap = [(-s, idx) for idx, s in enumerate(score)]
        ranked_scores = [0] * len(score)

        heapq.heapify(max_heap)

        rank = 1
        while max_heap:
            curr_score, idx = heapq.heappop(max_heap)
            ranked_scores[idx] = winners[rank] if rank <= 3 else str(rank)
            rank += 1

        return ranked_scores
        