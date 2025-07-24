class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        def get_char( k  )  :
            if k == 1 : 
                return 'a' 
            
            prev_len =  1 << ( t -1 ) 

            if k <= prev_len  : 
                return get_char(k) 
            
            else : 
                c = get_char( k - prev_len , t - 1 ) 

                return chr(( ord(c)  - ord('a' ) + 1 )  % 26 + ord('a' )  ) 
            

        t= 0  
        while( 1 << t  ) <  k :
            t += 1 

        return get_char(k ,  t ) 
        
