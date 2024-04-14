class Solution:
    '''
    Add 1 to the max_depth so far on each step as we go deeper into the tree
    Once we reach a non-node, return 0 as this has no depth then the 1s start acumulating from leaves to the root.
    '''
    def maxDepth(self, root) -> int:

        def dfs(node):
            if not node:
                return 0
            return 1 + max(
                dfs(node.left),
                dfs(node.right)
            )
        
        return dfs(root)