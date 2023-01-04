class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        currMin=prices[0]
        currMax=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<currMin:
                profit+=currMax-currMin
                currMin=prices[i]
                currMax=prices[i]
            elif currMax<prices[i]:
                currMax=prices[i]
            else:
                profit+=currMax-currMin
                currMin=prices[i]
                currMax=prices[i]
        profit+=currMax-currMin
        return profit