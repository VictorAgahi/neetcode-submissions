class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = float("inf")
        best_resell = float("-inf")
        for price in prices:
            if price < min_price:
                min_price = price
            if best_resell < (price - min_price):
                best_resell = price - min_price
        return best_resell
            
        