# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levels = {} # Create map for level total sums
        values = [] # create heap for level totals
        def helper(level, node):
            if level not in levels: levels[level] = 0 # create map entry for new levels
            levels[level] += node.val # summ all nodes on the level
            if node.left: helper(level + 1, node.left) # make recursive calls to children
            if node.right: helper(level + 1, node.right)
        helper(0, root) # initial function call
        for value in levels.values(): heapq.heappush(values, value * -1) # add level sums to heap
        for i in range(k): 
            if values: value = heapq.heappop(values) # pop value from heap if it exists
            else: return -1 # return -1 if the kth value is not found
        return value * -1 # return kth value