class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        maxProfit = 0
        n = len(prices)
        while r < n:
            if prices[r]>prices[l]:
                profit = prices[r] - prices[l]
                if profit>maxProfit:
                    maxProfit = profit
                r+=1
            else:
                l=r
                r+=1

        return maxProfit
            

