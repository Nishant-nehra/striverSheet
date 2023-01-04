class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1st method
        # maxProfit=0
        # minPrice=prices[0]
        # for i in range(1,len(prices)):
        #     minPrice=min(minPrice,prices[i])
        #     maxProfit=max(maxProfit,prices[i]-minPrice)
        # return maxProfit
        # 
        # 2nd Method
        maxProfit=0
        buy=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            maxProfit=max(maxProfit,prices[i]-buy)
        return maxProfit    