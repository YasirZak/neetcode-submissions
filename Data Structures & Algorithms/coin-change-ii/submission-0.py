class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        coins.sort()
        dp = {}

        def dfs(cs,amt,s=0):
            if amt==0: return 1
            if s>=n: return 0
            if (amt,s) in dp: return dp[(amt,s)]

            dp[(amt,s)]=0
            for d in range(amt//cs[s]+1):
                dp[(amt,s)]+=dfs(cs,amt-d*cs[s],s+1)

            return dp[(amt,s)]
            

        return dfs(coins,amount)