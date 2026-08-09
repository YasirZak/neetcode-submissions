class Solution:
    def isPalindrome(self, s:str) -> bool:
        i=0
        j=len(s)-1
        while i<j:
            if s[i]!=s[j]: return False
            i+=1
            j-=1
        return True

    def partition(self, s: str) -> List[List[str]]:
        if len(s)==0:
            return [[]]
        if len(s)==1:
            return [[s[0]]]

        res = []

        for i in range(len(s)):
            if self.isPalindrome(s[:i+1]):
                res.extend([j+[s[:i+1]] for j in self.partition(s[i+1:])])

        return res