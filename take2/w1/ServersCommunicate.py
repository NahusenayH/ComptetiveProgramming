class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        servRow = [0] * len(grid)
        servcol = [0] * len(grid[0])
        res = 0
        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    servRow[i] += 1
                    servcol[j] += 1
        
        for k in range (len(grid)):
            for l in range(len(grid[0])):
                if grid[k][l] == 1 and ((servRow[k] > 1) or (servcol[l] > 1)):
                    res += 1
        return res