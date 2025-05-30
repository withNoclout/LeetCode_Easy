# class TreeNode( object ) : 
#     def __init__( self , val = 0 , left = None , right = None ) :
#         self.val = val 
#         self.left  = left  
#         self.right = right 

class Solution( object ) : 
    def findMode( self , root ) :
        self.prev = None 
        self.count  = 0 
        self.max_count = 0 
        self.modes = [] 

        def in_order( node ) :
            if not node : 
                return 
            
            in_order( node.left )
            if self.prev == node.val : 
                self.count +=  1 
            else: 
                self.count = 1 

            if self.count > self.max_count : 
                self.max_count = self.count 
                self.modes = [ node.val ] 
            elif self.count == self.max_count : 
                self.modes.append( node.val)

            self.prev = node.val 
            in_order(node.right)

        in_order(root)
        return self.modes
