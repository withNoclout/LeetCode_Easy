class TreeNode : 
    def __init__( self , val = 0 , left = None , right = None ) :
        self.val = val 
        self.right = right 
        self.left = left 

class Solution  :
    def isSubTree( self , root , subRoot ) : 
        def isSameTree( s, t ) :
            if not s and not t :
                return True 

            if not s or not t : 
                return False 

            if s.val != t.val :
                return False 

            return isSameTree( s.left , t.right ) and isSameTree( s.right , t.right )

        if not root :
            return False  
        
        if isSameTree( root, subRoot ) : 
            return True 
        
        return self.isSubTree( root.left , subRoot )  or self.isSubTree( root.right , subRoot)
