def mincost( cost ): 
    n = len(cost ) 
    prev2 , prev1 = 0 ,0 
    for i in range( 0 , n + 1 ) : 
        curr  = min( prev1 , prev2  ) + (cost[i] if i < n else 0 )
        print( curr ) 
        prev2 = prev1 
        prev1 = curr 

    return prev1 

print( mincost([1,100,1,1,1,100,1,1,100,1] ))
