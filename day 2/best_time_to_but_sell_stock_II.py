#best time to buy & sell stock II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=1
        cp=prices[0]
        prof=0
        while i<len(prices):
            if prices[i]<=cp:
                cp=prices[i]
                i+=1
            elif prices[i]>cp:
                prof+=prices[i]-cp
                cp=prices[i]
                i+=1
        return prof


