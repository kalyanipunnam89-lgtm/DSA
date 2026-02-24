# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.total=0
        def dfs(node,curr):
            if not node:
                return 
            curr=(curr<<1)|node.val
            if not node.left and not node.right:
                self.total+=curr
                return
            dfs(node.left,curr)
            dfs(node.right,curr)
        dfs(root,0)
        return self.total            
        