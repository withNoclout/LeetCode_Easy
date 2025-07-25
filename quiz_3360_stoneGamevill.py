class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 10 : 
            return False 
        
        stones = n - 10 


        turn = 1 

        while stones > 0 : 
            if turn %2 == 0 : 
                stones -= 1 

            else : 
                stones -= 1 
            turn += 1 

        return False if stones == 0 else True 



# ===============  from solution 

