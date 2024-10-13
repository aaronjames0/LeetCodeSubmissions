# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node):
        if node.right:
            right = f"({self.helper(node.right)})"
            left_null = "()"
        else:
            right = ""
            left_null = ""
        if node.left: left = f"({self.helper(node.left)})"
        else: left = f"{left_null}"
        return f"{node.val}{left}{right}"

    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.helper(root)