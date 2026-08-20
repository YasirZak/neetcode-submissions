class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[0]*(n+1)
        if n==0: return res
        res[1]=1
        offset=2
        for i in range(2,n+1):
            if i==offset*2:
                offset=i
            res[i]=res[i-offset]+1

        return res