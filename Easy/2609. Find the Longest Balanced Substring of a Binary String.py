class Solution:
    '''
    solved this following the same approach as of 'longest palindromic substring'.
    consider every adjacent '01' as middle of the string and expand out both ways.
    then calculate the length and update the max_len.
    '''
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        max_len = 0
        valid_starts = []

        for i in range(len(s)-1):
            if s[i] == '0' and s[i+1] == '1':
                valid_starts.append((i, i+1))

        for i, j in valid_starts:
            while i > 0 and j < len(s)-1 and (s[i-1] == '0' and s[j+1] == '1'):
                i -= 1
                j += 1
            max_len = max(max_len, j - i +1)

        return max_len
        