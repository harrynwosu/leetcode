class Solution:
    def smallerNumbersThanCurrent(self, nums):
        '''
        Sort the array and map each number to its index in a hashmap
        The count of numbers a number is greater than will be its index in the sorted array
        In the case of duplicates, only store the index of the first occurence of the number since the subsequent occurences should have the same count as the first, plus its duplicates are not smaller than it
        '''
        hashmap = dict()
        sorted_nums = sorted(nums)
        res = [0] * len(nums)

        for idx, num in enumerate(sorted_nums):
            if num not in hashmap:
                hashmap[num] = idx
        
        for i in range(len(nums)):
            res[i] = hashmap[nums[i]]
        
        return res
        
