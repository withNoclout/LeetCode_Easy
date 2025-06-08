class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """

        self.x_depth = self.y_depth =  -1 
        self.x_parent = self.y_parent = None 

        def dfs( node , depth , parent ) :
            if not node : 
                return 
            
            if node.val ==x  : 
                self.x_depth = depth 
                self.x_parent = parent 
            elif node.val == y :
                self.y_depth = depth 
                self.y_parent = parent 

            dfs(    node.left , depth + 1 , node )
            dfs(    node.right , depth + 1 , node )

        dfs( root , 0 , None )

        return self.x_depth == self.y_depth and self.x_parent != self.y_parent
    
    
