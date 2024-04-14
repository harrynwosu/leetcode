class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        Intuition: 
            1. Prioritize removing larger digits from left to right if there are larger digits before smaller ones
            2. After this is k > 0 still, remove larger digits from right to left
        Approach: Use a monotonic increasing stack
        Why?:
            We want the resulting number to be in mostly increasing order as that minimizes it (caveat)
        Caveat: up until our limit for k.
        '''
        stack = []

        for digit in num:
            while stack and digit < stack[-1] and k:
                stack.pop()
                k -= 1
            stack.append(digit)

        while k > 0:
            stack.pop()
            k -= 1 
        
        '''
        This doesn't work for large test cases
        ValueError: Exceeds the limit (4300 digits) for integer string conversion: value has 9001 digits
        '''
        # return str(int("".join(stack))) if stack else "0"

        # Hence find the first non-zero digit in stack and start there
        if not stack or all([digit == "0" for digit in stack]):
            return "0"

        i = 0
        while stack[i] == "0":
            i += 1
        
        return "".join(stack[i:])
        