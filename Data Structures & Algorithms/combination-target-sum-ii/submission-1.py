class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(c,t,s=0):
            if t==0:
                return [[]]
            if t<0:
                return []

            res = []
            for i in range(s,len(c)):
                if i>s and c[i]==c[i-1]:
                    continue
                res+=[[c[i]]+j for j in helper(c,t-c[i],i+1)]

            return res

        candidates.sort()
        return helper(candidates,target)