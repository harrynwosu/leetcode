class Solution:
    def secondHighest(self, s: str) -> int:
        '''
        Add all the digits to a set
        Convert the set to a sorted list
        Return the second to last element in the sorted list if it exists, else -1
        '''
        digits_set = set()
        for char in s:
            if char.isnumeric():
                digits_set.add(char)
        
        digits_list = sorted(list(digits_set))

        return int(digits_list[-2]) if len(digits_list) > 1 else -1
        
        
        