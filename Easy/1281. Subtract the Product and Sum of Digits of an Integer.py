class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        total, product = 0, 1

        for val in str(n):
            total += int(val)
            product *= int(val)
        
        return product - total
        
        