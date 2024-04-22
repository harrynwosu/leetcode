from typing import List
from math import sqrt

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        '''
        Get all valid prime numbers and store them in an array
        Since you go in order, their indices are guaranteed to be in order
        So just return difference between the last occured prime and first occured prime
        '''
        #primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
        positions = []

        for idx, num in enumerate(nums):
            # if num in primes:
            #     positions.append(idx)
            if num > 1:  # 1 is not prime, so prevent going into the else condition
                for n in range(2, int(sqrt(num)) + 1):
                    if num % n == 0:
                        break
                else:
                    positions.append(idx)
        
        return positions[-1] - positions[0]

        