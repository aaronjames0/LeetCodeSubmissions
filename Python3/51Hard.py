class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        for i in range(n): solutions += self.helper([i], [0 + i], [0 - i], 1, n) # place a queen in the 0 row, ith column, and begin recursion with row 1
        self.parse(solutions, n)
        return solutions
    
    # row will be incremented with each recursive call. it is safe to assume it will never be occupied by another queen
    # we only need to find the open files, and open diagonals to know if a tile ([row, column]) is valid
    def helper(self, files, pos_diag, neg_diag, row, n):
        if len(files) == n: return [files] # every file is occupied by one safe queen, return 1 for this solution
        solutions = []
        for i in range(n): # try to insert at every file
            # to insert a queen: the file, positive sloping diagonal, and negative sloping diagonal must not be occupied
            if i not in files and (row + i) not in pos_diag and (row - i) not in neg_diag:
                # when a valid tile has been found, append it and continue the recursion
                solutions += self.helper(files + [i], pos_diag + [row + i], neg_diag + [row - i], row + 1, n)
        return solutions

    def parse(self, solutions, n):
        for i in range(len(solutions)):
            solution = solutions[i]
            for j in range(len(solution)):
                idx = solution[j]
                string = "." * n
                solution[j] = string[0:idx] + "Q" + string[idx + 1:]
            solutions[i] = solution