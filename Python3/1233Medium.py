class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res = []
        
        folder.sort() # sort the list of folders so subdirectories will follow directories above them
        
        for path in folder: # iterates the paths and append the first one, it will never be a subdirectory
            if not res or not path.startswith(res[-1] + "/"): res.append(path) # append a path when it does not start with the most recently added res path
        
        return res