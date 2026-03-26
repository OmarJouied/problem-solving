class Solution:
    def maxProfit(self, prices: list[int]) -> int:
      """
      You are given an array prices where prices[i] is the price of a given stock on the ith day.

      You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

      Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

      for ref:
      def maxProfit(self, prices: List[int]) -> int:
          maxi = 0
          for i in range(1,len(prices)):
              maxi = max(prices[i]-prices[i-1],maxi)
              prices[i] = min(prices[i-1],prices[i])
          return maxi

      def maxProfit(self, prices: List[int]) -> int:
          buy_price = prices[0]
          profit = 0

          for p in prices[1:]:
            if buy_price > p:
              buy_price = p
            
            profit = max(profit, p - buy_price)
          
          return profit
      """
      res = 0

      min = prices[0]
      for i in range(1, len(prices)):
        if min > prices[i]:
          min = prices[i]
        elif prices[i] - min > res:
          res = prices[i] - min

      return res
