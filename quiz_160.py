class solution( object ) : 
    def getIntersectionNode( self  , headA , headB   ) : 
        if not headA or not headB  : 
            return False 
        pA , pB = headA , headB

        while pA != pB : 
            pA = pA.next if pA else headB  
            pB = pB.next if pB else headA 

        return pA 
