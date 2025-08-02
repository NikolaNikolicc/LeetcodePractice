from collections import deque

# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        outputList = []
        queue = deque()
        queue.append(root)

        while len(queue):
            levelList = []
            for i in range(len(queue)):
                node = queue.popleft()
                levelList.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            outputList.append(levelList)

        return outputList
