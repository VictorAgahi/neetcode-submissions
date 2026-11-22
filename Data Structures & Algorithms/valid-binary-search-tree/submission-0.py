class Solution:
    def dfs(self, node, min_val, max_val):
        if not node:
            return True
            
        if not (min_val < node.val < max_val):
            return False

        return (self.dfs(node.left, min_val, node.val) and 
                self.dfs(node.right, node.val, max_val))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))