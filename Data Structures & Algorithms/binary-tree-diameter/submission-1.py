class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def height(node):
            if not node:
                return 0
            
            left_h = height(node.left)
            right_h = height(node.right)
            
            self.max_diameter = max(self.max_diameter, left_h + right_h)
            
            return 1 + max(left_h, right_h)
        
        height(root)
        return self.max_diameter