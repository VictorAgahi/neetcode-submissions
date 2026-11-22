# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []
        current_level = []
        queue.append(root)
        queue.append(None)
        while queue:
            node = queue.popleft()
            if not node:
                continue
            node_level = [node]
            n = queue.popleft()
            while n:
                node_level.append(n)
                n = queue.popleft()

            for n in node_level:
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
                current_level.append(n.val)
            queue.append(None)
            res.append(current_level)
            current_level = []
        return res