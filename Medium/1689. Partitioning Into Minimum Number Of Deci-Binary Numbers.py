class Solution:
    '''
    The trick to this problem is to discover that the minimum number of positive deci-binary numbers needed will always be the maximum digit in the given input number.
    Why: 
        Since we are able to add up only 1s and 0s, to a sum that is equl to that maximum digit, max, we need exactly max number of 1s.
        This is the only way we can get the number as it is the upper bound and major constraint
        All other numbers can be gotten by some other smart permutations of the 0s and 1s we use to sum.
    '''
    def minPartitions(self, n: str) -> int:
        return max(int(char) for char in n)