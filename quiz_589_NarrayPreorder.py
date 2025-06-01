class Node  : 
    def __init__( self, val = 0 , children = None ) : 
        self.val = val 
        self.children = children if children is not None else [] 


class Solution  :
    def preorder( self , root ) :
        result = []

        def dfs( node ) :
            if not node : 
                return 
            
            result.append( node.val )

            for child in node.children  : 
                dfs(child)

        dfs(root )

        return result 
