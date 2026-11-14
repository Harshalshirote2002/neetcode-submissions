class TreeNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.oldest = TreeNode(key = "oldest", val="oldest")
        self.latest = TreeNode(key = "latest", val="latest")

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        return node.key
    
    def insert(self, node):
        prevNode = self.latest.prev
        prevNode.next = node
        self.latest.prev = node
        node.next = self.latest
        node.prev = prevNode
        return node


    def get(self, key: int) -> int:
        # print(self.cache.keys())
        node = self.cache.get(key, None)

        if node is None:
            return -1
        
        self.remove(node)
        self.insert(node)

        return node.val

        

    def put(self, key: int, value: int) -> None:
        # print(self.latest.prev, self.oldest.next, key, value)
        if not self.latest.prev or not self.oldest.next:
            # print("wasn't here then")
            newNode = TreeNode(key=key, val=value, prev=self.oldest, next=self.latest)
            self.latest.prev = newNode
            self.oldest.next = newNode
            self.cache[key] = newNode
            return
        if self.cache.get(key) is None:
            newNode = TreeNode(key=key, val=value)
            self.cache[key] = self.insert(newNode)

        if len(self.cache) > self.capacity:
            to_remove = self.remove(self.oldest.next)
            # print(f"key removed: {to_remove}")
            del self.cache[to_remove]
        
        
        node = self.cache.get(key)
        node.val = value
        self.remove(node)
        self.insert(node)

        return



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)