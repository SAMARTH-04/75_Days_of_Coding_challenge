# Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        l=[]
        cp=prices[0]
        prof=0
        for i in range(len(prices)):
            if prices[i]<cp:
                cp=prices[i]
            elif prices[i]>cp:
                if prices[i]-cp>prof:
                    prof=prices[i]-cp
        return prof
