

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        s1 = prices[0]
        s2 = prices[0]
        middle_low = prices[0]
        for i in range(len(prices)):
            
            if prices[i] >s2 :
                s2 = prices[i]
            
            if prices[i] <middle_low:
                middle_low = prices[i]

            if s2-s1 <= prices[i] - middle_low:
                s2 = prices[i]
                s1 = middle_low


        return s2-s1 
