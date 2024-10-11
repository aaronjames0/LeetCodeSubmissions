class Solution:
    def hasFresh(self, grid):
        for row in grid:
            if 1 in row: return True
        return False

    def rot(self, grid, i, j, len1, len2):
        adj = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        changed = []
        for y, x in adj:
            if 0 <= i + y < len1 and  0 <= j + x < len2 and grid[i + y][j + x] == 1:
                grid[i + y][j + x] = 2
                changed.append([i + y, j + x])
        return changed

    def minute(self, grid, len1, len2):
        changed = []
        for i in range(len1):
            for j in range(len2):
                if grid[i][j] == 2 and [i,j] not in changed:
                    changed = self.rot(grid, i, j, len1, len2) + changed
        return grid

    def copyGrid(self, grid):
        copy = []
        for row in grid:
            copy.append(row.copy())
        return copy

    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        len1 = len(grid)
        len2 = len(grid[0])
        while self.hasFresh(grid):
            last = self.copyGrid(grid)
            last = [cell[:] for cell in grid]
            grid = self.minute(grid, len1, len2)
            if last == grid: return -1
            else: res += 1
        return res