class ListNode( object  ) : 
    def __init__(self ,  val = 0 , left= None , right =None ) : 
        self.val  = val 
        self.next  = next  
        self.right = right 


class Solution( object )  : 
    def binaryTreePaths( self , root )  :
        result =  [] 

        def dfs( node , path )  :
            if not node : 
                return 
            
            path +=  str( node.val ) 

            if not node.left and not node.right : 
                result.append( path ) 
                return 
            
            path +=  "->"

            dfs(node.left  , path )
            dfs(node.right , path )

        dfs( root , '' ) 
        return result
