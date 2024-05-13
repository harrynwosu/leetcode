from typing import List

class Solution:
    '''
    Use bottom-up iterative dp to pre-compute later energies first
    '''
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        
        dp = [ float("-inf") ] * len(energy)
        
        for i in range(len(energy) - 1, -1, -1):
            if i + k >= len(energy):
                dp[i] = energy[i]
            else:
                dp[i] = energy[i] + dp[i+k]
        
        return max(dp)                