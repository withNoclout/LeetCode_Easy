class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        amount.sort()

        max_val = amount[2] 

        sum_rest = amount[0] + amount[1] 

        if max_val > sum_rest : 
            return max_val 
        
        return (sum( amount ) + 1) // 2 
