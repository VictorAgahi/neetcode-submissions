class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            if in_left > in_right:
                return None
                
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            node = TreeNode(root_val)
            mid = inorder_map[root_val]
            node.left = helper(in_left, mid - 1)
            node.right = helper(mid + 1, in_right)
            
            return node
            
        return helper(0, len(inorder) - 1)