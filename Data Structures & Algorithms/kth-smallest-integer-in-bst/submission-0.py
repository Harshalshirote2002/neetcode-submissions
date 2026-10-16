# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        sorted_array = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)

            nonlocal sorted_array
            sorted_array.append(root.val)

            dfs(root.right)

        dfs(root)

        return sorted_array[k-1]
