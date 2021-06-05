# https://leetcode.com/problems/lru-cache/
# medium

class Node:
    def __init__(self,key,val):
        self.key = key
        self.value = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = 0
        self.cache = {}
    
        self.head = None
        self.tail = None
        self.capacity = capacity

    def get(self, key: int) -> int:
        if (key in self.cache):
            self._remove(self.cache[key])
            self._push(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        
        if (key in self.cache):
            x = self._remove(self.cache[key])
            self.size-=1
            
        elif (self.size >= self.capacity):
            x = self._remove(self.tail)
            if x.key in self.cache:
                del self.cache[x.key]
            self.size-=1
            
        self.cache[key] = Node(key,value)
        self._push(self.cache[key])
        self.size+=1
        
            
    def _push(self, node):
        if (self.head == None):
            self.tail = node
            self.head = node
            return
        self.head.prev = node
        node.next = self.head
        self.head = node
        if (self.tail == None):  self.tail == self.head.next

    def _remove(self, node):      
        if (node == self.head):
            if (node.next != None):
                self.head = node.next
                node.prev = None
            else:
                self.head = None
                self.tail = None
            return node
        
        elif (node == self.tail):
            if (node.prev != None):
                self.tail = node.prev
                node.prev.next = None
            else: 
                self.tail = None
            return node

        node.prev.next = node.next
        node.next.prev = node.prev
        return node
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(4)
# param_1 = obj._push(Node(2))
# print(param_1.next.value)

