class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        def countPalindrome(s,l,r):
            if l<0 or r>=n: return 0
            if s[l]==s[r]:
                return 1+countPalindrome(s,l-1,r+1)
            return 0

        res=0
        for size in range(2):
            for l in range(n-size):
                r=l+size
                res+=countPalindrome(s,l,r)

        return res  