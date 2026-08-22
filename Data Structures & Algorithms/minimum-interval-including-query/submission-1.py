class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries_idx = [(q,i) for i,q in enumerate(queries)]
        queries_idx.sort()
        j=0
        h=[]


        res=[-1]*len(queries)
        for q,i in queries_idx:
            while j<len(intervals) and intervals[j][0]<=q:
                s,e=intervals[j]
                heapq.heappush(h,(e-s+1,e))
                j+=1
            while h and h[0][1]<q:
                heapq.heappop(h)
            if h:
                res[i]=h[0][0]
        return res
