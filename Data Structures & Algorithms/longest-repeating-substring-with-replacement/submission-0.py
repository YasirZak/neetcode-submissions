class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        i=0
        j=0
        cur_k=0
        res=0
        while j<=len(s):
            if len(map)!=0:
                cur_k= (j-i) - max(map.values())

            if cur_k > k:
                map[s[i]]-=1
                i+=1
            else:
                res = max(res, j-i)
                if j<len(s):
                    if s[j] not in map.keys():
                        map[s[j]]=0
                    map[s[j]]+=1   
                j+=1

        return res