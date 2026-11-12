class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        smallest = prices[0]
        biggest_profit = 0

        for price in prices:
            if price - smallest > biggest_profit:
                biggest_profit = price - smallest
            if price < smallest:
                smallest = price
        
        return biggest_profit