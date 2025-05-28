class Solution(object ) : 
    def sumOfLeftLeaves( self , root ) :
        if not root : 
            return 0 
        
        total = 0 

        if root.left and not root.left.left and not root.right.right : 
            total += root.left.val 


        return total + self.sumOfLeftLeaves( root.left )  + self.sumOfLeftLeaves( root.right)
