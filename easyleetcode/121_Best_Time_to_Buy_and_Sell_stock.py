class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=10**6
        maxprofit=0
        for i in prices:
            if i<minprice:
                minprice=i
            if i-minprice>maxprofit:
                maxprofit=i- minprice
        return maxprofit