class Solution:
    def sumNumbers(self, root) -> int:
        '''
        Use a stack to incrementally add and pop node values from the tree during dfs
        We only get a full number once we reach a leaf
        So once we reach a leaf concatenate the digits in the current stack as that will be the whole number from the root to that leaf, then add this number to the global sum
        We pop a node value from a stack only when we are done exploring its children since no other number will be formed through that node.
        '''
        self.sum = 0
        self.stack = []

        def dfs(node):
            if not node:
                return 
            
            self.stack.append(node.val)
            if not (node.left or node.right):
                self.sum += int("".join([str(digit) for digit in self.stack]))
            
            dfs(node.left)
            dfs(node.right)
            self.stack.pop()
        
        dfs(root)
        return self.sum