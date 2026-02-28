"""
Q.121 https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
T(N) : O(n)
Space Complexity : O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = prices[0]
        max_price = 0

        for price in prices:
            max_price = max(max_price , price - min_price)
            min_price = min(min_price,price)

        return max_price
        
