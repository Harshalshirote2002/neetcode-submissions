# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            level = []
            for i in range(len(queue)):
                item = queue.pop(0)
                level.append(item.val)
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            result.append(level)

        response = []
        for level in result:
            if level:
                response.append(level[-1])

        return response