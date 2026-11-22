# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isEqual(self, p1, p2):
        if not p1 and not p2:
            return True
        if not p1 or not p2:
            return False
        if p1.val != p2.val:
            return False
        return self.isEqual(p1.right, p2.right) and self.isEqual(p1.left, p2.left)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return not subRoot
        if root.val == subRoot.val:
            found = self.isEqual(root, subRoot)
            if found:
                return True
        left = self.isSubtree(root.left, subRoot) 
        if left:
            return True
        right = self.isSubtree(root.right, subRoot)
        return right