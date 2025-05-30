class TreeNode( object )  : 
    def __init__( self, val = 0 , left =None , right = None ) : 
        self.val = val 
        self.left = left 
        self.right = right 
class Solution( object ) : 
    def getMinimumDifference( self , root)   : 
        self.prev = None 
        self.min_diff = float('inf')

        def in_order( node ) : 
            if not node : 
                return  
            
            in_order  (node.left )

            if self.prev is not None : 
                self.min_diff = min ( self.mid_diff , abs( node.val - self.prev ) )

            self.prev = node.val 

            in_order( node.right ) 

        in_order(root)
        return self.min_diff 
