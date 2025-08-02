# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isValidBSTUptimal(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower, upper):

            if not node:
                return True

            if node.val <= lower or node.val >= upper:
                return False

            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)  

        return dfs(root, float("-inf"), float("inf"))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower, upper):

            if node.val >= upper or \
               node.val <= lower or \
               (node.left and node.left.val >= node.val) or \
               (node.right and node.right.val <= node.val):
               return False

            if not node.right and not node.left:
                return True

            if node.left and node.val > node.left.val:
                if not dfs(node.left, lower, node.val):
                    return False

            if node.right and node.val < node.right.val:
                if not dfs(node.right, node.val, upper):
                    return False

            return True        

        return dfs(root, float("-inf"), float("inf"))