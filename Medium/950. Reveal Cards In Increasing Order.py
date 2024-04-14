from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck):
        '''
        Sort the deck. The result array should be the sorted elements placed in a new array skipping one index every time
        [2, __ , 3, __ , 5, __ , 7] -> next index in queue is 1 but we skip the next index after an append
        So append 11 at index 3 -> [2, __ , 3, 11 , 5, __ , 7]
        We can use a queue for the indices to implement this
        '''
        n = len(deck)
        res = [0] * n # initialize result array
        deck.sort()
        q = deque(range(n))  # Create original queue of indices

        for num in deck:
            idx = q.popleft()
            res[idx] = num
            if q:
                q.append(q.popleft())

        
        return res

        