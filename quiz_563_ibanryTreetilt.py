class TreeNode : 
    def __init__( self , val = 0 , right = None , left = None ) :
        self.val =val 
        self.left = left 
        self.right  = right 

class Solution :
    def findTilt ( self , root ) :
        self.total_tilt = 0 
        def dfs( node  ) : 
            if not node :
                return  0 
            
            left_sum = dfs( node.left) 
            right_sum = dfs( node.right )

            tilt = abs( left_sum - right_sum)

            self.total_tilt += tilt 

            return left_sum  + right_sum + node.val 
        
        dfs(root)
        return self.total_tilt 
    
    o

