class Node : 
    def __init__( self , val = 0 , children = None ) :
        self.val = val 
        self.children = children if children is not None else [] 

class Solution : 
    def postorder ( self, root ) :
        result = [] 
        def dfs( node ) :
            if not node : 
                return 
            for child in node.children : 
                dfs(child) 

            result.append(node.val)

        dfs( root ) 

        return result  
