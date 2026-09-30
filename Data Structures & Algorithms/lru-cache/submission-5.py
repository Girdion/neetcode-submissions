class Node:
    
    def __init__(self, key, value):

        self.next = None
        self.prev = None

        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head
    
    # MRU <-> A <-> B <-> LRU
    # MRU <-> A <-> LRU
    # MRU <-> B <-> A <-> LRU

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_head(self, node):
        node.next = self.head.next
        node.prev = self.head

        node.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:

        if key not in self.cache: return -1

        node = self.cache[key]

        self.remove_node(node)
        self.add_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:

            node = self.cache[key]
            node.value = value

            self.remove_node(node)
            self.add_head(node)
        
        else:

            self.cache[key] = Node(key, value)

            node = self.cache[key]

            self.add_head(node)
        
        if len(self.cache) > self.capacity:

            lru = self.tail.prev

            self.remove_node(lru)

            print(lru.key)
            print(self.cache)

            del self.cache[lru.key]
        


            