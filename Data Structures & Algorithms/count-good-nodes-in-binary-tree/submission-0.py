# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, root, local_max):
        if not root:
            return 0
        current_max = local_max
        if root.val >= current_max:
            return 1 + self.dfs(root.left, root.val) + self.dfs(root.right, root.val)
        return self.dfs(root.left, current_max) + self.dfs(root.right, current_max)

    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, float('-inf'))
        