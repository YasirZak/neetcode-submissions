class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def sinkLand(grid, i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=="0":
                return

            grid[i][j]="0"
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                sinkLand(grid,i+di,j+dj)

        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    res+=1
                    sinkLand(grid,i,j)

        return res