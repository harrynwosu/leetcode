class Solution:
    '''
    This stores the complements of a seen number in a hashmap
    If we encounter a number that exists in the hashmap, that mean we must have come across its complement, so return.
    '''
    def twoSum(self, nums, target):
        comps = {}
        for idx in range(len(nums)):
            if nums[idx] in comps:
                return idx, comps[nums[idx]]
            comps[target-nums[idx]] = idx