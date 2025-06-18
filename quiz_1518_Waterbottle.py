class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total_drunk = numBottles
        empty_bottles = numBottles
        while empty_bottles  >= numExchange: 
            new_full = empty_bottles // numExchange
            total_drunk += new_full
            empty_bottles = new_full + (empty_bottles % numExchange)
        return total_drunk 
