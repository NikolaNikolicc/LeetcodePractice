# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        
        if not preorder or not inorder or len(preorder) == 0 or len(inorder) == 0:
            return None

        hashInorder = {val: index for index, val in enumerate(inorder)}

        readPreorder = [0]
    
        def construct(start, end):

            if start > end or start > len(inorder) - 1 or end < 0:
                return None

            node = TreeNode(preorder[readPreorder[0]])
            separator = hashInorder[preorder[readPreorder[0]]]
            readPreorder[0] += 1

            startLeft, endLeft = start, separator - 1
            startRight, endRight = separator + 1, end

            node.left = construct(startLeft, endLeft)
            node.right = construct(startRight, endRight)

            return node

        return construct(0, len(preorder) - 1)