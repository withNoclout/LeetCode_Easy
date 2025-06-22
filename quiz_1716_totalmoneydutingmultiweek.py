class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        weeks = n// 7  
        days_left = n % 7
        total = 0 

        for k in range(weeks ) : 
            total += 28 + 7 * k

        start = 1 + weeks 
        for i in range( days_left) : 
            total += start  + i 

        return total 
