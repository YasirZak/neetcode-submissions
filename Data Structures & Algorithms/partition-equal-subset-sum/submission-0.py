class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {}
        def check(n, s1=0, s2=0, c=0):
            if c==len(n):
                if s1==s2: return True
                return False

            if (s1,s2,c) in dp: return dp[(s1,s2,c)]

            dp[(s1,s2,c)] = check(n,s1+n[c],s2,c+1) or check(n,s1,s2+n[c],c+1)
            return dp[(s1,s2,c)]

        return check(nums)