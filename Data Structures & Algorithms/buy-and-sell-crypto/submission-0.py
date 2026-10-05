class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        cheapest = prices[0]

        for i in range (1, len(prices)):
            if prices[i] < cheapest:
                cheapest = prices[i]
                continue
            
            if prices[i] - cheapest > maxp:
                maxp = prices[i] - cheapest
            
        return maxp
        