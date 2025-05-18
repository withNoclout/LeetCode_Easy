class Solution(object) : 
    def isbalanced( self , root ) : 
        def check( node ) : 
            left = check(node.left) 
            right = check(node.right ) 
            if left == -1 : 
                return -1 
            if right == -1 : 
                return -1 
            
            if abs( left - right ) > 1 : 
                return -1 
            
            return 1 + max( left , right )
        
        return check(root ) != -1 
