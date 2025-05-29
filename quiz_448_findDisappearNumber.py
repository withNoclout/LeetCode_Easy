class Solution( object )  :
    def findDisappearedNumber( self , nums ) :
        for num in nums : 
            index = abs( num)  -1 
            if nums[ index ]  > 0 :
                nums[ index ] *= - 1 
        result = [] 
        for i in range( len(num) ) :
            if nums[i]  > 0 :
                result.append( i +1 ) 
        return result 
