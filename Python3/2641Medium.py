# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0 # replace values at depths 0 and 1 as they have no cousins

        if root.left: root.left.val = 0
        if root.right: root.right.val = 0

        depths = {} # create a map for depths to their totals

        def total_depths(node, depth):
            if depth == 0 or depth == 1: # skip depths 0 and 1, call their children recursively
                if node.left: total_depths(node.left, depth + 1)
                if node.right: total_depths(node.right, depth + 1)
            else:
                if depth not in depths: depths[depth] = 0 # add node values to depths value map and call children recursively
                depths[depth] += node.val
                if node.left: total_depths(node.left, depth + 1)
                if node.right: total_depths(node.right, depth + 1)

        total_depths(root, 0) # get the depths totals map

        def replace_vals(node, depth): # iterate through nodes and replace values
            children = 0 # total value of a node's children
            if depth == 0: # skip depth 0
                if node.left:
                    replace_vals(node.left, depth + 1)
                if node.right:
                    replace_vals(node.right, depth + 1)
            else: # total a node's children
                if node.left:
                    children += node.left.val
                    replace_vals(node.left, depth + 1)
                if node.right:
                    children += node.right.val
                    replace_vals(node.right, depth + 1)
                if node.left: node.left.val = depths[depth + 1] - children # replace children values with
                if node.right: node.right.val = depths[depth + 1] - children # depths[depth + 1] - children

        replace_vals(root, 0) # call the replacement function then return root node

        return root