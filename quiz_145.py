class solution( object  ) :
    def prost( self , root ) : 
        result = []  
        def dfs( node ) :
            dfs( node.left )
            dfs( node.right  )
            result.append( node.value )
        dfs(root)

        return result 
