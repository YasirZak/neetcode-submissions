class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = {}
        for i in range(numCourses):
            prereq_map[i] = []

        for i,j in prerequisites:
            prereq_map[i].append(j)
        
        res = []

        visit, cycle = set(), set()     

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq_map[crs]:
                if dfs(pre)==False:
                    return False

            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True

        for i in range(numCourses):
            if dfs(i)==False:
                return []

        return res