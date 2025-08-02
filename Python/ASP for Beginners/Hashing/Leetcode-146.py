# https://leetcode.com/problems/lru-cache/description/

from typing import List

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self):
        return "(val: " + str(self.val) + "; prev: " + (str(self.prev.val) if self.prev else "None") + "; next: " + (str(self.next.val) if self.next else "None") + ")"

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.jobs = {}
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, key: int) -> Node:
        node = self.jobs[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def insert(self, key: int, node: Node) -> None:
        node.next = self.tail
        node.prev = self.tail.prev
        node.prev.next = self.tail.prev = node

    def get(self, key: int) -> int:
        val = -1
        if key in self.jobs:
            node = self.remove(key)
            val = node.val
            self.insert(key, node)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.jobs:
            self.remove(key)
        self.jobs[key] = Node(key, value)
        self.insert(key, self.jobs[key])
        
        if self.cap < len(self.jobs):
            node = self.head.next
            self.remove(node.key)
            self.jobs.pop(node.key)

lru = LRUCache(2)
lru.put(1, 10)
lru.put(2, 20)
lru.put(3, 30)
print(lru.jobs)
# print(lru.get(1))