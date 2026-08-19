class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        neighbors = {}
        for i,j in edges:
            if i not in neighbors:
                neighbors[i]=[]
            neighbors[i].append(j)
            if j not in neighbors:
                neighbors[j]=[]
            neighbors[j].append(i)

        for i,j in reversed(edges):
            s = deque()
            visit = set([i])
            for v in neighbors[i]:
                if v!=j:
                    s.append(v)

            while s:
                v=s.pop()
                if v==j: return [i,j]
                if v in visit: continue
                visit.add(v)
                for c in neighbors[v]:
                    s.append(c)

