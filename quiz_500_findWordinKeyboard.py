class Solution( object ) :
    def findWords( self , words ) :
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        result = [] 

        for word in words : 
            lower_set =  set( word.lower()) 

            if lower_set.issubset(row1) or lower_set.issubset(row2 )  or lower_set.issubset(row3):
                result.append(word) 

        return result 
