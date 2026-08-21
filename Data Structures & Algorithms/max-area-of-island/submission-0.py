class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def countAndSink(i,j):
            nonlocal count
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==0:
                return
            
            count+=1
            grid[i][j]=0
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                countAndSink(i+di,j+dj)

        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    count=0
                    countAndSink(i,j)
                    res=max(res,count)

        return res