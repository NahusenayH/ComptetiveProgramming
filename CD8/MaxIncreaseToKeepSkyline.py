class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: 
            return 0
        
        rows = [0] * len(grid)
        cols = [0] * len(grid[0])
        for i in range(len(grid)):
            rows[i] = max(grid[i][j] for j in range(len(grid[0])))
        for j in range(len(grid[0])):
            cols[j] = max(grid[i][j] for i in range(len(grid)))
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += min(rows[i], cols[j]) - grid[i][j]
        return ans
                