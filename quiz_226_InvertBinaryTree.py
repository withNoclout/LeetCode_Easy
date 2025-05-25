class TreeNode( self ) : 
    self.val = val 
    self.left = left 
    self.right = right 

class Solution( object ) : 
    def invertTree( self , root ) : 
        if not root :
            return None 

        root.left , root.right = self.invertTree( root.right ) , self.invertTree( root.left ) 

        return root 
