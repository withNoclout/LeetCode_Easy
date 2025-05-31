class Node:
    def __init__ ( self , val = None , children = None ) :
        self.val = val 
        self.children = children if children is not None else [] 


class Solution: 
    def maxDepth( self , root ) :
        if not root :
            return  0 
        if not root.children : 
            return 1 
        
        max_child_depth = 0  
        for child in root.children : 
            max_child_depth = max( max_child_depth , self.maxDepth( child))

        return max_child_depth + 1 o

