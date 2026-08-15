class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        s_map = {}
        t_map = {}
        for i in s:
            if i not in s_map:
                s_map[i]=0
            s_map[i]+=1

        for i in t:
            if i not in t_map:
                t_map[i]=0
            t_map[i]+=1

        for i in t_map.keys():
            if i not in s_map:
                return False

        for i in s_map.keys():
            if i not in t_map:
                return False
            if s_map[i]!=t_map[i]:
                return False

        return True