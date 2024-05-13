class Solution:
    '''
    If n is a multiple of 2 return it, else return the next multiple of 2, which is n*2
    '''
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n%2 == 0 else n*2