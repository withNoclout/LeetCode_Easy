from collections import Counter
class Solution( object): 
    def rcanConstruct( self , ransomenote , magazine ) : 
        ransom_count = Counter(magazine) 
        magazine_count = Counter(magazine)
        for chat in ransomenote : 
            if ransom_count[char] > magazine_count[char] :
                return False    
        return True 
