class Solution( object)  : 
    def selfDividingNumbers( self , left , right ) : 
        result = [] 

        for num in range( left, right + 1 ) :
            if self.isSelfDiving(num) : 
                result.append( num ) 

        return result  
    
    def isSelfDiving( self,  num  ) :
        temp = num 
        while  temp > 0  : 
            digit = temp % 10 
            if digit == 0 or num % digit != 0 :
                return False 
            temp //= 10 
        return True 
    

   
