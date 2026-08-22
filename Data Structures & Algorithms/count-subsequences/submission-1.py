class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        lookup={}
        def count(i,j):
            if j>=m:
                return 1
            if i>=n:
                return 0
            if (i,j) not in lookup:
                lookup[(i,j)]=0
                if s[i]==t[j]:
                    lookup[(i,j)]+=count(i+1,j+1)
                lookup[(i,j)]+=count(i+1,j)
            return lookup[(i,j)]

        res=0
        for i in range(n):
            if s[i]==t[0]:
                res+=count(i+1,1)

        return res
