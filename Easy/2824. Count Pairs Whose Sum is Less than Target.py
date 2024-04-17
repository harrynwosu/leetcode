class Solution:
    def countPairs(self, nums, target):
        '''
        Sort the array and use two pointers, one from start and one from end of nums
        If the sum of the elements at left and right is less than the target value, it means all pairs with the current left element (from curr left to al elements to left of right) will also satisfy the condition. So, increment the count by right - left and move the left pointer to the right.
        If the sum is greater than or equal to the target, move the right pointer to the left.
        '''
        i, j = 0, len(nums) - 1
        nums.sort()
        count = 0

        while i < j:
            curr_sum = nums[i] + nums[j]
            if curr_sum < target:
                count += j - i
                i += 1
            else:
                j -= 1

        return count