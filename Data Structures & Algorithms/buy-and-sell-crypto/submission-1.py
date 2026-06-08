class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        maxProfit = 0
        minPrice = max(prices)
        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                profit = price - minPrice
                maxProfit = max(profit, maxProfit)
        return maxProfit

        