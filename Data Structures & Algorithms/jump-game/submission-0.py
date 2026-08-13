class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n==1: return True
        table = [False]*n
        table[-1]=True

        for i in range(n-2,-1,-1):
            for j in range(1,nums[i]+1):
                if i+j<n and table[i+j]:
                    table[i]=True
                    break

        return table[0]