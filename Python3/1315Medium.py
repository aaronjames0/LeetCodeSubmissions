# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def helper(node): # recursive helper function
            if not node: return 0 # if the node does not exist, return 0
            res = 0
            if node.val % 2 == 0: # if the node value is even
                if node.left: # if it has a left child, check left grandchildren and add the values
                    if node.left.left: res += node.left.left.val
                    if node.left.right: res += node.left.right.val
                if node.right: # if it has a right child, check right grandchildren and add the values
                    if node.right.left: res += node.right.left.val
                    if node.right.right: res += node.right.right.val
            if node.left: res += helper(node.left) # recursively call on the left child if it exists
            if node.right: res += helper(node.right) # recursively call on the right child if it exists
            return res
        return helper(root)