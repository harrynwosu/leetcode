from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root):
        '''
        Important: Inorder traversal iterates a BST in sorted order
        No Hashmap Approach : 
        Keep track of current streak of numbers
        Initailize current streak and max streak to 0
        If we encounter a current streak that is greater than max streak, update max streak
        '''
        curr_streak, max_streak, curr_num = 0, 0, 0
        res = []

        def dfs(node):
            nonlocal curr_streak, max_streak, curr_num, res
            if not node:
                return
            
            dfs(node.left)

            if node.val == curr_num:
                curr_streak += 1
            else:
                curr_streak = 1
                curr_num = node.val

            if curr_streak == max_streak:
                res.append(curr_num)
            
            elif curr_streak > max_streak:
                res = [curr_num]
                max_streak = curr_streak
            
            

            dfs(node.right)
        
        dfs(root)

        return res

    '''
    Brute force: Use hashmap to store frequencies and return maxes
    '''
    
    def findMode2(self, root):
        freq = defaultdict(int)

        def dfs(node):
            if not node:
                return
            freq[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        
        res = []
        max_freq = max(freq.values())

        for num, count in freq.items():
            if count == max_freq:
                res.append(num)

        return res