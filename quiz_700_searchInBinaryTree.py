class Solution: 
    def searchBST( self , root , val )  :
        while root : 
            if root.val == val : 
                return root 
            elif val < root.val : 
                root = root.left 
            else : 
                root = root.right 
        return None 
