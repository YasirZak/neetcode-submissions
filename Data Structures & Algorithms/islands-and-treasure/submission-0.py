class Solution:
    def fill_all(self, grid: List[List[int]], i, j, m, n, val=0):
        grid[i][j]=val

        if i+1<m and grid[i+1][j]!=-1 and grid[i+1][j]>val+1:
            self.fill_all(grid, i+1, j, m, n, val+1)
        if j+1<n and grid[i][j+1]!=-1 and grid[i][j+1]>val+1:
            self.fill_all(grid, i, j+1, m, n, val+1)
        if i-1>=0 and grid[i-1][j]!=-1 and grid[i-1][j]>val+1:
            self.fill_all(grid, i-1, j, m, n, val+1)
        if j-1>=0 and grid[i][j-1]!=-1 and grid[i][j-1]>val+1:
            self.fill_all(grid, i, j-1, m, n, val+1)


    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])

        treasures = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    treasures.append((i,j))

        for (i,j) in treasures:
            self.fill_all(grid, i, j, m, n)

        