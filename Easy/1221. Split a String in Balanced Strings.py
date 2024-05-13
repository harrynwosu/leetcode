class Solution:
    '''
    Keep track of the counts of the Rs and Ls.
    Whenever the two counts become equal, we have found one substring.
    So increase result count by 1, reset the two counts to 0 and continue.
    '''
    def balancedStringSplit(self, s: str) -> int:
        r_count, l_count = 0, 0
        res = 0

        for char in s:
            if char == "R":
                r_count += 1
            else:
                l_count += 1
            
            if r_count == l_count:
                res += 1
                r_count = 0
                l_count = 0
        
        return res

        