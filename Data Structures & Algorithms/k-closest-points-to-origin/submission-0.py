class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h=[]
        for i,(x,y) in enumerate(points):
            heapq.heappush(h,(y**2+x**2,i))

        res=[]
        for i in range(k):
            if h:
                _,idx=heapq.heappop(h)
                res.append(points[idx])

        return res