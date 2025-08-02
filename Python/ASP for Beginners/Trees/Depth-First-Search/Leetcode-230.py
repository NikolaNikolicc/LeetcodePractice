# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def iterative(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        curr = root
        stack = []

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            cnt += 1
            if cnt == k:
                return curr.val

            curr = curr.right

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        cnt = 0
        res = -1

        def inorder(root):
            nonlocal cnt, res
            
            if not root:
                return None
            
            inorder(root.left)

            cnt += 1

            if cnt == k:
                res = root.val
                return
            inorder(root.right)

        inorder(root)
        return cnt