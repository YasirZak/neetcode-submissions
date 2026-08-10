class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]

        for src,dst in prerequisites:
            adj[src].append(dst)

        cycle, visit = set(), set()

        def dfs(src):
            if src in cycle:
                return False
            if src in visit:
                return True

            cycle.add(src)
            for i in adj[src]:
                if dfs(i)==False:
                    return False
            cycle.remove(src)
            visit.add(src)

            return True

        for i in range(numCourses):
            if dfs(i)==False:
                return False

        return True