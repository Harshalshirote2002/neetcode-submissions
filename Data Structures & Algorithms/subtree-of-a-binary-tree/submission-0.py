# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        if not root:
            return False

        def isValid(root, subRoot):
            if root and subRoot:
                if root.val == subRoot.val:
                    return isValid(root.left, subRoot.left) and isValid(root.right, subRoot.right)
                else:
                    return False

            elif root and not subRoot:
                return False
            elif subRoot and not root:
                return False
            else:
                return True


        if isValid(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)




        