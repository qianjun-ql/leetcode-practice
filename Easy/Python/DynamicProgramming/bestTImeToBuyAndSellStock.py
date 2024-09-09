# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Initialize min_price to a large number and max_profit to 0
        min_price = float('inf')
        max_profit = 0
        
        # Traverse through all the prices
        for price in prices:
            # Update the minimum price if a lower price is found
            if price < min_price:
                min_price = price
            
            # Calculate the current profit by subtracting the min_price from the current price
            current_profit = price - min_price
            
            # Update the maximum profit if the current profit is greater than the max_profit
            if current_profit > max_profit:
                max_profit = current_profit
        
        return max_profit