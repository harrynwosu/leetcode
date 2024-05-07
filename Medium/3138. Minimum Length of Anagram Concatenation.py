import math
from collections import Counter


class Solution:
    def minAnagramLength(self, s: str) -> int:
        '''
        The minimum length is the sum of all frequencies divided by the GCD of frequencies
        '''
        freq = Counter(s)

        # Find the GCD of frequencies
        gcd = freq[s[0]]
        for count in freq.values():
            gcd = math.gcd(gcd, count)

        min_len = sum(freq.values()) // gcd

        return min_len
            
        
        