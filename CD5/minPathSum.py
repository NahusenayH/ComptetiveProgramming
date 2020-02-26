class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        path = grid
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    prev = 0
                elif i == 0:
                    prev = path[i][j-1]
                elif j == 0:
                    prev = path[i-1][j]
                else:
                    prev = min(path[i-1][j], path[i][j-1])
                path[i][j] = prev + grid[i][j]
        return path[m-1][n-1]
        