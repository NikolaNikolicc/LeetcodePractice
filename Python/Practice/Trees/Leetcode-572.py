# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            
            if node1 and node2 and node1.val == node2.val:
                return dfs(node1.right, node2.right) and \
                dfs(node1.left, node2.left)

            return False

        if not root:
            return False

        if root.val == subRoot.val:
            if dfs(root, subRoot):
                return True
                
        return self.isSubtree(root.left, subRoot) or \
        self.isSubtree(root.right, subRoot)
        