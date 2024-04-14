class Solution:
    '''
    Approach 1:
    1. Perform normal tree dfs however, pass a boolean flag down the tree for each node to indicate if it is a left node or not (True/False)
    2. If we encounter a leaf node, we check its boolean flag. If true, add its value to the result
    '''
    def sumOfLeftLeaves(self, root):
        self.curr_sum = 0

        def dfs(node, left):
            if not node:
                return

            if not (node.left or node.right) and left:
                self.curr_sum += node.val
            
            dfs(node.left, True)
            dfs(node.right, False)

        dfs(root, False)
        return self.curr_sum
    
    '''
    Approach 2:
    1. Perform normal tree dfs
    2. For each parent node we check if it has a left child
    3. If this parent has a left child, check if this left child is a leaf by checking if it has no left and right children itself
    4. If true, add the value of this left child to the global result
    '''
    def sumOfLeftLeaves2(self, root):
        curr_sum = 0

        def dfs(node):
            nonlocal curr_sum   # makes this variable available in global scope, essential for recursion
            if not node:
                return
            if node.left and (not node.left.left and not node.left.right):
                curr_sum += node.left.val
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return curr_sum
    