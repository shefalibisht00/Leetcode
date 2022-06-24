class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left, right = 0,1
        maxProfit = 0
        
        while right<len(prices):
            
            # If Profitables 
            if prices[right]>prices[left]:
                newProfit = prices[right]-prices[left]
                maxProfit = max(maxProfit, newProfit)
            else:
                left = right
            
            right+=1
                         
        return maxProfit
        