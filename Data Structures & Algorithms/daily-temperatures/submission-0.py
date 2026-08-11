class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n

        for i in range(n-1,-1,-1):
            if i==n-1:
                res[i]=0
            else:
                comp = 1
                while i+comp<n:
                    if temperatures[i+comp]>temperatures[i]:
                        res[i]=comp
                        break
                    else:
                        if res[i+comp]==0:
                            res[i]=0
                            break
                        comp+=res[i+comp]

        return res
