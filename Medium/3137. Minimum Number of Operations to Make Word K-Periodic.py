from collections import defaultdict

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        freq = defaultdict(int)
        
        for i in range(0, len(word), k):
            freq[word[i : i+k]] += 1
        
        substring_count = len(word) // k
        max_value = max(freq.values())
        
        return substring_count - max_value
        