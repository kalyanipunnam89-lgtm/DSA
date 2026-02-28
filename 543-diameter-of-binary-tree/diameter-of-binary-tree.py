# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        def help(node):
            if not node:
                return 0
            lh = help(node.left)
            rh = help(node.right)
            self.diameter = max(self.diameter, lh + rh)
            return 1 + max(lh,rh)
        help(root)
        return self.diameter        
        