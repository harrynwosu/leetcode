class Solution:
    def longestIdealString_cached(self, s: str, k: int) -> int:
        '''
        Memory Limit Exceeded
        DP problem where the two choices are including a letter or skipping a letter
        '''
        cache = dict()

        def helper(i, prev):
            if i == len(s):
                return 0
            
            if (i, prev) in cache:
                return cache[(i, prev)]
            
            # Choice 1: Skip current character
            res = helper(i + 1, prev)

            # Choice 2: Include current character
            if prev == "" or abs(ord(s[i]) - ord(prev)) <= k:  # Only if their absolute differnce is 
                res = max(res, 1 + helper(i + 1, s[i]))

            cache[(i, prev)] = res

            return res

        return helper(0, "")    # Start with first character at idx 0 and no previous char
    
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26

        for char in s:
            curr = ord(char) - ord('a')
            longest = 1
            
            for prev in range(26):
                if abs(curr - prev) <= k:
                    longest = max(longest, 1 + dp[prev])
            dp[curr] = longest
        
        return max(dp)
        