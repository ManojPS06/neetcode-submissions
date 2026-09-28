class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0 
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]#[10,1,5,6,7,1] best=6
                if profit > best:
                    best = profit
        return best