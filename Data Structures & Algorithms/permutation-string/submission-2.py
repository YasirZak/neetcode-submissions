class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n=len(s1),len(s2)
        if n<m: return False

        counts={}
        for l in s1:
            if l not in counts:
                counts[l]=0
            counts[l]+=1

        for i in range(n-m+1):
            if s2[i] in counts:
                temp_counts = counts.copy()
                j=i
                while j<n and s2[j] in temp_counts:
                    temp_counts[s2[j]]-=1
                    if temp_counts[s2[j]]==0:
                        del temp_counts[s2[j]]
                    j+=1
                if not temp_counts: return True

        return False