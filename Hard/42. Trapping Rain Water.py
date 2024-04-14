class Solution:
    def trap(self, height):
        '''
        The amount of water that can be trapped at each element is equal to the minimum of 
        the two maximum heights of all walls to the left and right of the curr position => min(maxleft, maxRight)
        minus the height of the element itself. => min(maxleft, maxRight) - currheight

        Notice: one of these max heights is always going to be the overall maximum height in the array
        so just to find the maximums to the left and right of this overall max using 2 loops
        '''
        water = 0
        max_height, max_height_idx = max(height), height.index(max(height))

        # For left side of max_height
        max_left = height[0]
        for i in range(1, len(height[:max_height_idx])):
            if height[i] > max_left:
                max_left = height [i]
            else:
                water += max_left - height[i]

        # For right side of max_height
        max_right = height[-1]
        for i in range(len(height) - 1, max_height_idx, -1):
            if height[i] > max_right:
                max_right = height [i]
            else:
                water += max_right - height[i]

        return water
        