class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        '''
        For each base in the range get the representation of the number in that base
        Convert that representation to a string and compare it with its reverse
        At any point they are not equal return False
        If loop completes without breaking, return True
        '''
        for i in range(2, n+1):
            base_rep = self.num_to_base(n, i)
            num = str(base_rep)
            reversed_num = num[::-1]
            if num != reversed_num:
                return False

        return True
    
    def num_to_base(self, num, base):
            new_num = ""

            while num > 0:
                new_num = str(num % base) + new_num
                num = int(num / base)
            
            return new_num