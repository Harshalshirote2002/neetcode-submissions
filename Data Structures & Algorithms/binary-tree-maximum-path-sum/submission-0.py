# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxSum = -float("inf")

        def dfs(root):
            if not root:
                return 0
            tot = 0
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            nonlocal maxSum
            maxSum = max(maxSum, root.val + left + right)

            return root.val + max(left, right)

        dfs(root)
        return maxSum



