# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root # store the root node
        self.size = 0 # declare the size int
        self.get_size(self.root) # get the size

    def get_size(self, node):
        if node: # if a node exists
            self.size += 1 # increment the size
            self.get_size(node.left) # call the function on children recursively
            self.get_size(node.right)

    def get_path(self):
        size = self.size + 1 # calculate the path to reach the last node in a complete tree of size self.size + 1
        path = "" # declare the size string
        while size != 1: # iterate until the root is reached
            if size % 2 == 0: path = "L" + path # 1-based indexing - an even number means it is a left child
            else: path = "R" + path # odd numbers mean it is a right child
            size = size // 2 # the parent will have an index of index // 2
        return path

    def insert(self, val: int) -> int:
        curr = self.root # start at the root
        for step in self.get_path(): # get and iterate through the path needed to reach the next open node
            if step == "L": # Left step
                if curr.left: curr = curr.left # if a left child exists, update curr and continue
                else: # if a left child does not exist
                    parent = curr.val # save the value of the current node
                    curr.left = TreeNode(val) # create the new node
            else: # Right step, same logic as above, just for the right child
                if curr.right: curr = curr.right
                else:
                    parent = curr.val
                    curr.right = TreeNode(val)
        self.size += 1 # increment the size
        return parent

    def get_root(self) -> Optional[TreeNode]:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()