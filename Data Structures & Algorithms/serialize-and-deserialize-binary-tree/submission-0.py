# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        depth = 0
        response = []
        queue = [root]
        val = []
        depth = 0

        def bfs(queue):
            nextQueue = []
            res = []
            # levelLength = 2**depth
            valFound = False
            while queue:
                node = queue.pop(0)
                if node:
                    res.append(node.val)
                    valFound = True
                    if node.left and node.right:
                        nextQueue.append(node.left)
                        nextQueue.append(node.right)
                    elif node.left and not node.right:
                        nextQueue.append(node.left)
                        nextQueue.append(None)
                    elif node.right and not node.left:
                        nextQueue.append(None)
                        nextQueue.append(node.right)
                    else:
                        nextQueue.append(None)
                        nextQueue.append(None)
                else:
                    res.append(None)
                    # nextQueue.append(None)
                    # nextQueue.append(None)
            return res, nextQueue, valFound

        res, nextQueue, valFound = bfs(queue)
        response.extend(res)

        while nextQueue and valFound:
            depth+=1
            res, nextQueue, valFound = bfs(nextQueue)
            response.extend(res)

        response = response[:2**depth-1]
        responseStr = [str(item) for item in response]
        print(",".join(responseStr))
        return ",".join(responseStr)


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = data.split(",")

        data = [int(item) if item!="None" else None for item in data]

        root = TreeNode(data.pop(0))
        queue = [root]
        depth = 2

        def assignNodes(nodes, children):
            if not children:
                return [], True, []
            childNodes = []
            allNone = True
            # print(nodes)
            while nodes:
                leftChild = None
                rightChild = None
                left=None
                if children:
                    left = children.pop(0)
                right = None
                if children:
                    right = children.pop(0)
                if left is not None:
                    leftChild = TreeNode(left)
                if right is not None:
                    rightChild = TreeNode(right)
                if leftChild:
                    childNodes.append(leftChild)
                if rightChild:
                    childNodes.append(rightChild)
                node = nodes.pop(0)
                if node:
                    # print(node)
                    allNone = False
                    node.left = leftChild
                    node.right=rightChild

            return childNodes, allNone, children



        # children = data[(2**(depth-1))-2: (2**depth)-2]
        children = data

        # print(children)

        nodes, allNone, children = assignNodes(queue, children)

        while nodes and not allNone:
            depth += 1
            # children = data[(2**(depth-1))-2: (2**depth)-2]
            # print(children)
            nodes, allNone, children = assignNodes(nodes, children)
            # print(nextRoots, data)

        return root
            
        



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))