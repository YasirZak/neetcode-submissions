class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i=0
        j=0
        while(j<len(prices)):
            if(prices[j]-prices[i]<0): i=j
            else:
                res = max(res,prices[j]-prices[i])
                j+=1

        return res