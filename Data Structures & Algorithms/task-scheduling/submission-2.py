class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for i in tasks:
            if i not in counts:
                counts[i]=0
            counts[i]+=1

        pq = []
        for task,count in counts.items():
            heapq.heappush_max(pq,(count,task))

        res = 0
        q = deque()
        while pq or q:
            if len(pq)==0 and len(q)!=0:
                while q[0]=='*':
                    q.popleft()
                    res+=1
                if len(q)>0:
                    heapq.heappush_max(pq, q.popleft())

            if len(q)!=0:
                ele = q.popleft()
                if ele != '*':
                    heapq.heappush_max(pq,ele)

            count,task = heapq.heappop_max(pq)
            res+=1

            if count-1 != 0:
                while len(q)<n:
                    q.append('*');
                q.append((count-1,task))

        return res
