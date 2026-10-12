# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        result = True

        def dfs(root):
            if not root:
                return 0

            l_depth = 0
            r_depth = 0

            if root.left:
                l_depth = 1 + dfs(root.left)
            if root.right:
                r_depth = 1 + dfs(root.right)

            if abs(l_depth - r_depth) > 1:
                
                nonlocal result

                result = False
            
            return max(l_depth, r_depth)

        dfs(root)

        return result