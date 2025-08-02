# https://leetcode.com/problems/range-sum-query-mutable/

class Node:
    def __init__(self, L, R, val = 0):
        self.val = val
        self.R = R
        self.L = L
        self.left = None
        self.right = None

class NumArray(object):

    def __init__(self, nums):
        
        def build(L, R):
            node = Node(L, R)

            if L == R:
                node.val = nums[L]
                return node
            M = (L + R) // 2
            node.left = build(L, M)
            node.right = build(M + 1, R)
            node.val = node.left.val + node.right.val
            
            return node

        self.root = build(0, len(nums) - 1)
        

    def update(self, index, val):
        
        def update_helper(node):

            M = (node.L + node.R) // 2
            if node.R == node.L:
                node.val = val
                return
            elif index > M:
                update_helper(node.right)
            else:
                update_helper(node.left)

            node.val = node.left.val + node.right.val

        update_helper(self.root)
        

    def sumRange(self, left, right):
        
        def sum_helper(node):
            
            if left <= node.L and node.R <= right:
                print("uslo")
                print(node.L)
                print(node.R)
                return node.val

            if node.L > right or node.R < left:
                return 0

            return sum_helper(node.left) + sum_helper(node.right)

        return sum_helper(self.root)
        


# Your NumArray object will be instantiated and called as such:
nums = [1,3,5]
obj = NumArray(nums)
# obj.update(index,val)
left, right = 0, 2
param_2 = obj.sumRange(left,right)