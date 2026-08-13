class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return 0
        dp = [float('inf')]*n
        dp[-1]=0

        for i in range(n-2,-1,-1):
            for j in range(1,nums[i]+1):
                if i+j>n-1: break
                dp[i]=min(dp[i],1+dp[i+j])

        return dp[0]