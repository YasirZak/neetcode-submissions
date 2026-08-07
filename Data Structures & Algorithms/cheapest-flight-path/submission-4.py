class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dist = [1000*100]*n
        dist[src]=0

        for i in range(k+1):
            tmpDist = dist.copy()
            for u,v,p in flights:
                if dist[u] != 1000*100 and dist[u]+p < tmpDist[v]:
                    tmpDist[v] = dist[u]+p
            dist = tmpDist

        if dist[dst]==1000*100:
            return -1
        
        return dist[dst]