from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        '''
        If we divide equally, the sum of each partition is guaranteed to be sum(array) // 3
        Use sliding window to check if all the partitions have sum of sum(array) // 3
        '''
        partition_sum = sum(arr) // 3
        partition_count = 0
        i, j = 0, 1

        while j < len(arr):
            curr_sum = arr[i]
            # Increase window until we get sum that = expected partition_sum
            while j < len(arr) and curr_sum != partition_sum:
                curr_sum += arr[j]
                j += 1
            
            # Increase our number of valid partitions (sum == expectedpartition_sum)
            partition_count += 1

            # Move to next window
            i = j
            j += 1

            # If we have 2 partition already and the rest of the list sums up to our expected_partition_sum, that is the third partition, so return True
            if partition_count == 2 and (i < len(arr) and sum(arr[i:]) == partition_sum):
                return True

    
        return False


        