# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        baseVal = root.val

        def dfs(root, baseVal):
            if not root:
                return 0

            maxVal = max(baseVal, root.val)
            if root.left and root.right:
                return int(root.val>=baseVal) + dfs(root.left, maxVal) + dfs(root.right, maxVal)
            if root.left and not root.right:
                return int(root.val>=baseVal) + dfs(root.left, maxVal)
            if root.right and not root.left:
                return int(root.val>=baseVal) + dfs(root.right, maxVal)
            if not root.left and not root.right:
                return int(root.val>=baseVal)
            
            return 0

        return dfs(root, baseVal)
