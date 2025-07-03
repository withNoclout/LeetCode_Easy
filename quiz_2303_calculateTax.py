class Solution(object):
    def calculateTax(self, brackets, income):
        """
        :type brackets: List[List[int]]
        :type income: int
        :rtype: float
        """
        tax = 0 
        prev = 0 
        

        for upper , percent in brackets :
            if income > prev :
                taxable = min( income , upper ) - prev 
                tax += taxable * ( percent / 100 ) 
                prev = upper 
            else : 
                break 

        return round( tax , 5 )
