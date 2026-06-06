class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        suffixArr = [0]

        n = len(prices)
        for i in range(n-2, -2, -1):
            maxSuffix = suffixArr[0]
            if prices[i+1] > maxSuffix:
                suffixArr.insert(0, prices[i+1])
            else:
                suffixArr.insert(0, maxSuffix)

        maxProfit = 0
        for i in range(n):
            profit = suffixArr[i] - prices[i]
            if profit > maxProfit:
                maxProfit = profit

        return maxProfit

