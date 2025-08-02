# https://leetcode.com/problems/path-sum/submissions/1511003985/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        currSum = [0]

        def dfs(root):
            if not root:
                return False

            currSum[0] += root.val

            if currSum[0] == targetSum and not root.left and not root.right:
                return True

            if dfs(root.left):
                return True
            
            if dfs(root.right):
                return True

            currSum[0] -= root.val
            return False

            
        return dfs(root)
