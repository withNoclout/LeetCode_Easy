class Solution( object ) :
    def findPoisonedDuration( self , timeSeries  , duration ) :
        if not timeSeries : 
            return 0 
        
        total = 0 
        for i in range ( 1, len( timeSeries)) : 
            total += min( timeSeries[i] - timeSeries[i-1 ] , duration)

        total += duration

        return total 
