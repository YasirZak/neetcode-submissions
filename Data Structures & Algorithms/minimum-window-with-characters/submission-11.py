class Solution:
    def minWindow(self, s: str, t: str) -> str:        
        t_m= {}
        for w in t:
            if w not in t_m:
                t_m[w]=0
            t_m[w]+=1

        i=0
        need = len(t_m)
        have = 0
        s_m = {}
        res=float('inf')
        res_str=""
        for j in range(len(s)):

            if s[j] not in s_m:
                s_m[s[j]]=0
            s_m[s[j]]+=1
            
            if s[j] in t_m and s_m[s[j]]==t_m[s[j]]:
                have+=1

            while have==need:
                if j-i+1<=res:
                    res_str=s[i:j+1]
                    res=len(res_str)
                # if i==j: break
                s_m[s[i]]-=1
                if s[i] in t_m and s_m[s[i]]<t_m[s[i]]:
                    have-=1
                i+=1


        return res_str