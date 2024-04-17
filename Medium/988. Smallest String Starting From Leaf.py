# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def smallestFromLeaf(self, root) -> str:
        '''
        Keep track of a global smallest, if we see a string less than this smallest, update it. At the end, return the final global smallest
        How do we loop through the different strings?
            1. Have a helper function that converts the numbers to characters using ASCII notation
            2. Use a var, curr to track how far we are in the construction of a string
            3. Perform dfs on the tree, passing the current string w/ the node
            4. At each node, using our transformation helper function convert the number to the char and append it to the left of the current char so the string is in reverse order, i.e from node to root, not root to node
            5. If we get to a leaf, update smallest if necessary. If this is the first leaf ensure smallest is set to the current string and not the empty starting string for smallest so subsequent comparisons are correct
            6. If not, recusrsively call dfs on the left and right children of the current node passing in the new curr string
        '''
        self.smallest = ""

        def get_char(num):
            return chr(97 + num) # ASCII lowercase starts from 97, 'a' -> 97

        def dfs(node, curr):
            if not node: return

            curr = get_char(node.val) + curr

            if not (node.left or node.right):
                self.smallest = min(self.smallest, curr)  if self.smallest != "" else curr
            
            dfs(node.left, curr)
            dfs(node.right, curr)

        dfs(root, "")
        return self.smallest






        