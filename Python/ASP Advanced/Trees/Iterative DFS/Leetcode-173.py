# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        self.stack = []

        node = root
        while node:
            self.stack.append(node)
            node = node.left

        

    def next(self):
        retVal = self.stack.pop()
        curr = retVal.right
        while curr:
            self.stack.append(curr)
            curr = curr.left

        return retVal.val
        

    def hasNext(self):
        return True if self.stack else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()