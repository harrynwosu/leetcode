# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        '''
        Perform post order traversal on the tree calculating the sums and count of the left and right nodes of each node
        At each node return its sum and total count
        '''
        count = 0

        def dfs(node):
            nonlocal count

            if not node:
                return 0, 0
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            if (node.val + left_sum + right_sum) // (left_count + right_count + 1) == node.val:
                count += 1
            return (left_sum + right_sum + node.val), (left_count + right_count + 1)
        
        dfs(root)
        return count

        