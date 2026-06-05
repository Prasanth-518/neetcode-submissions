class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        b=prices[0]
        for i in prices:
            if profit < i-b:
                profit = i-b
            if i <= b:
                b = i
        return profit