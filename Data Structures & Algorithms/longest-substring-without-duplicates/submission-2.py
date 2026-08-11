class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n<=1: return n
        count = defaultdict(int)
        i=0
        j=0
        res=0
        count[s[0]]+=1

        while j<n-1:
            j+=1
            count[s[j]]+=1
            while count[s[j]]>1:
                count[s[i]]-=1
                i+=1
            res = max(res,j-i+1)

        return res