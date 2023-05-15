
class Node:
    def __init__(self, value=None, key=None):
        self.value = value
        self.key = key
        self.next = self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.the_cache = {}
        self.right, self.left = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node

    def insert(self, node):
        prev_node, next_node = self.right.prev, self.right
        prev_node.next = next_node.prev = node
        node.next = next_node
        node.prev = prev_node

    def get(self, key):
        if key in self.the_cache:
            new_node = Node(self.the_cache[key].value, key)
            self.remove(self.the_cache[key])
            self.insert(new_node)
            self.the_cache[key] = new_node
            return self.the_cache[key].value
        else:
            return -1

    def put(self, key, value):
        if key in self.the_cache:
            self.remove(self.the_cache[key])
            del self.the_cache[key]
        new_node = Node(value, key)
        self.insert(new_node)
        self.the_cache[key] = new_node
        if len(self.the_cache) > self.capacity:
            the_key = self.left.next.key
            self.remove(self.left.next)
            del self.the_cache[the_key]


