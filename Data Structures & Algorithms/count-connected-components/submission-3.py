class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        m = {}

        for node in range(n):
            m[node] = []

        for i,j in edges:
            m[i].append(j)
            m[j].append(i)

        res = 0
        visited = []
        for node in range(n):
            if node not in visited:
                res+=1
                to_visit = [node]
                while len(to_visit)!=0:
                    visited.append(to_visit[0])
                    for child in m[to_visit[0]]:
                        if child not in visited:
                            to_visit.append(child)
                    to_visit = to_visit[1:]

        return res
