class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while True:
            s.add(n)
            c=n
            n=0
            while c:
                n+=(c%10)**2
                c//=10
            if n==1: return True
            if n in s: return False
