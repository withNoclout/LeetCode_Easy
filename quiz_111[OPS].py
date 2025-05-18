class Solution(object) : 
    def minDepth( self , root ) : 
        if not root :
            return 0 
        queue = [( root , 1 )]
        while queue : 
            node , depth = queue.pop()
            if not node.left and node.right : 
                return depth 
            if node.left  : 
                queue.append((node.left  , depth +1 ))
            if node.right  : 
                queue.append(( node.right , depth + 1 ))
                
