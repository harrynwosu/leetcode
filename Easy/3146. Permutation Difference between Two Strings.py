class Solution:
    '''
    Use two hashmaps to store the indices of each character in the two different strings
    '''
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_map = {}
        t_map = {}
        
        for idx, char in enumerate(s):
            s_map[char] = idx
        for idx, char in enumerate(t):
            t_map[char] = idx
        
        res = 0
        
        for char in s:
            res += abs(s_map[char] - t_map[char])
        
        return res
    