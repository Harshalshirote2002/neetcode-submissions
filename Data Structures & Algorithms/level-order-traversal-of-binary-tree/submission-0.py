# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        queue = [root]
        result = []

        if not root:
            return []

        def levelOrder(queue):
            nextQueue = []
            result = []
            while queue:
                item = queue[0]
                result.append(item.val)
                if item.left:
                    nextQueue.append(item.left)
                if item.right:
                    nextQueue.append(item.right)
                queue = queue[1:]

            return result, nextQueue

        while queue:
            res, queue = levelOrder(queue)
            result.append(res)

        return result


            