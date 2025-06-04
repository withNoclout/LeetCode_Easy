class Solution( object)  : 
    def minCostClimbingStair( self , cost ) : 
        n = len( cost ) 
        prev2 , prev1 = 0 , 0 

        for i in range( 1 , n+1 ) :
            curr = min( prev1 , prev2 ) + ( cost[i] if i < n else 0 )

            prev2 = prev1 
            prev1 = curr 

        return prev1 
     
