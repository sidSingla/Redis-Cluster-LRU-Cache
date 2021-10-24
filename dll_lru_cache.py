# Class LRUCache is using Doubly Linked List(DLL)  for addition, removal flexibility. 
# A dict is used to maintain key-value cache.

from collections import dict

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.cache:
            n = self.cache[key]
            self.remove(n)
            self.add(n)
            return n.val
        return -1

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        n = Node(key, value)
        self.add(n)
        self.cache[key] = n
        if len(self.cache) > self.capacity:
            n = self.head.next
            self.remove(n)
            del self.cache[n.key]

    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail