class Solution : 
    def findSecondMinimumValue( self , root ) :
        min_val = root.val 
        self.second_min = float('inf')

        def dfs(node ) :
            if not node : 
                return 
            if min_val < node.val < self.second_min :
                self.second_min = node.val 
            elif node.val == min_val :
                dfs( node.left ) 
                dfs( node.right ) 

        dfs(root) 
        return self.second_min if self.second_min < float('inf') else  - 1 	

