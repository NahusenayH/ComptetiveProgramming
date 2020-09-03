class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start =(0,0)
        length = 0
        for ro in range(len(grid)):
            for co in range(len(grid[0])):
                if grid[ro][co] == 0:
                    length += 1
                if grid[ro][co] == 1:
                    start = (ro,co)
        visited = set()
        rows = len(grid) 
        cols = len(grid[0])
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        result = [0]
        def dfs(cur):
            if cur in visited or not (0 <= cur[0] < rows) or not(0 <= cur[1] < cols) or grid[cur[0]][cur[1]]==-1:
                return
            visited.add(cur)
            if len(visited)==length+2 and grid[cur[0]][cur[1]]==2:
                    result[0]+=1
                
            for direction in directions:
                next_i = cur[0] + direction[0]
                next_j = cur[1] + direction[1]
                visited.add(cur)
                dfs((next_i, next_j))
            visited.remove(cur)
            
        dfs(start)
        return result[0]
        