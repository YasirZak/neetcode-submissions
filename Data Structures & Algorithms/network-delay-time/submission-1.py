class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges={}
        for i,j,d in times:
            if i not in edges:
                edges[i]=[]
            edges[i].append((j,d))
        # print(edges)

        dist=[-1]*n
        s=[(0,k)]

        while(s):
            # print(s)
            d,i=heapq.heappop(s)
            if dist[i-1]!=-1 and d>=dist[i-1]:
                continue
            dist[i-1]=d
            if i in edges:
                for j,e in edges[i]:
                    heapq.heappush(s,(d+e,j))

        # print(dist)
        if min(dist)==-1: return -1
        return max(dist)