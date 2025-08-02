# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def inorderTraversalIterative(self, root):
        stack = []
        outputList = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            outputList.append(curr.val)
            curr = curr.right
            
            
        return outputList

# stack: 1
# curr = 1
# outputList:  

    # recursive
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        outputList = []

        def dfs(root):
            if not root:
                return None

            dfs(root.left)
            outputList.append(root.val)
            dfs(root.right)

        dfs(root)
        return outputList