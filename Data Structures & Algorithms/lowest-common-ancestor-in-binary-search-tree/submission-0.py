# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def isMid(root, p, q):
            if not root:
                return False
            if root.val > p.val and root.val> q.val:
                return isMid(root.left, p, q)
            elif root.val<p.val and root.val<q.val:
                return isMid(root.right, p, q)
            else:
                return root

        result = isMid(root, p, q)
        if not result:
            return root
        else:
            return result
                
            