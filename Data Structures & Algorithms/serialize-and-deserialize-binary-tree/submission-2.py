from collections import deque

class Codec:
    def serialize(self, root):
        if not root:
            return ""
        
        res = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("#")
                
        return ",".join(res)

    def deserialize(self, data):
        if not data:
            return None
            
        vals = iter(data.split(","))
        root = TreeNode(int(next(vals)))
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            # Process left child
            val = next(vals)
            if val != "#":
                node.left = TreeNode(int(val))
                queue.append(node.left)
            
            # Process right child
            val = next(vals)
            if val != "#":
                node.right = TreeNode(int(val))
                queue.append(node.right)
                
        return root