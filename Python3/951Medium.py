# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2: return True # return true if both roots are null pointers
        if (not root1 and root2) or (root1 and not root2): return False # return false if only one root is a null pointer
        if root1.val != root2.val: return False # return false if the root values do not match
        return self.helper(root1, root2) # return the main call to the recursive helper function

    def helper(self, node1, node2):
        # return true if both nodes are null
        if not node1.left and not node1.right and not node2.left and not node2.right: return True
        # if only left children exist
        elif node1.left and not node1.right and node2.left and not node2.right:
            # make a recursive call if their values match
            if node1.left.val == node2.left.val: return self.helper(node1.left, node2.left)
            # otherwise return False
            else: return False
        # if only right children exist
        elif node1.right and not node1.left and node2.right and not node2.left:
            # make a recursive call if their values match
            if node1.right.val == node2.right.val: return self.helper(node1.right, node2.right)
            # otherwise return False
            else: return False
        # if the nodes only have one of opposing children
        elif node1.left and not node1.right and node2.right and not node2.left:
            # the childrens value are equal, could be a flip, make recursive call
            if node1.left.val == node2.right.val: return self.helper(node1.left, node2.right)
            # otherwise return False
            else: return False
        # if the nodes only have one of opposing children
        elif node1.right and not node1.left and node2.left and not node2.right:
            # the childrens value are equal, could be a flip, make recursive call
            if node1.right.val == node2.left.val: return self.helper(node1.right, node2.left)
            # otherwise return False
            else: return False
        # if both nodes have both children
        elif node1.left and node1.right and node2.left and node2.right:
            # if the children match their same sides
            if node1.left.val == node2.left.val and node1.right.val == node2.right.val:
                return self.helper(node1.left, node2.left) and self.helper(node1.right, node2.right)
            # if the children match their opposite sides
            elif node1.left.val == node2.right.val and node1.right.val == node2.left.val:
                return self.helper(node1.left, node2.right) and self.helper(node1.right, node2.left)
            # if neither one is a match
            else: return False
        else: return False