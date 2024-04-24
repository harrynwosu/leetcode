from functools import lru_cache
from typing import List

class Solution:
    @lru_cache(maxsize=None)
    def tribonacci(self, n: int) -> int:
        # cached recursive function - Time: O(n), Space: O(n)
        if n == 0:
            return 0
        if n <= 2:
            return 1
        
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

    def tribonacci2(self, n: int) -> int:
        # dp array - Time: O(n), Space: O(n)
        dp = [0, 1, 1] + [0] * (n-2)
        print(dp)

        if n <= 2:
            return dp[n]
        
        for i in range(3, n+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

        return dp[n]
    
    def tribonacci3(self, n: int) -> int:
        # iterative - Time: O(n), Space: O(1)
        a, b, c = 0, 1, 1

        for _ in range(n):
            a, b, c = b, c, a + b + c
        
        return a
