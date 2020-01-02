#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        length = len(prices)-1
        sp = prices[length]
        profit = 0
        for i in range(length-1,-1,-1):
            cp = prices[i]
            if profit < sp-cp:
                profit = sp-cp
            sp = max(cp,sp)
        return profit
