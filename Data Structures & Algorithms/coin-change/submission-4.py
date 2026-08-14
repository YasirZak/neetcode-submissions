class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}
        def recursive(cs,amt):
            if amt==0: return 0
            if amt in mem: return mem[amt]

            mem[amt]=float('inf')
            for c in cs:
                if c<=amt:
                    mem[amt]=min(mem[amt],1+recursive(cs,amt-c))

            return mem[amt]

        res=recursive(coins,amount)
        if res==float('inf'): return -1
        return res
            