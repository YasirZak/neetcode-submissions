class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # implementing dikstras
        m,n=len(grid),len(grid[0])
        dist={}
        h=[(0,0,(0,0))]
        c=1

        while h:
            d,_,(i,j) = heapq.heappop(h)
            if (i,j) in dist and dist[(i,j)]<=d:
                continue
            dist[(i,j)]=d
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                if i+di>=0 and i+di<m and j+dj>=0 and j+dj<n:
                    # time=grid[i+di][j+dj]-grid[i][j] if grid[i+di][j+dj]>grid[i][j] \
                    # else grid[i][j]
                    maxs=max(grid[i+di][j+dj],grid[i][j])
                    t=maxs-d if maxs>d else 0
                    heapq.heappush(h,(d+t,c,(i+di,j+dj)))
                    c+=1

        return dist[(m-1,n-1)]