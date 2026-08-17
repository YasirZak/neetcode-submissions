class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = {
            1: set(),
            2: set()
        }

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    m[grid[i][j]].add((i,j))

        res=0
        while m[1]:
            noSpread=True
            spread=set()
            for i,j in m[2]:
                for di,dj in [(0,1),(1,0),(0,-1),(-1,0)]:
                    if i+di>=0 and i+di<len(grid) and j+dj>=0 and j+dj<len(grid[0]):
                        if (i+di,j+dj) in m[1]:
                            noSpread=False
                            spread.add((i+di,j+dj))

            if noSpread: return -1
            res+=1

            for i in spread:
                m[1].remove(i)
                m[2].add(i)

        return res