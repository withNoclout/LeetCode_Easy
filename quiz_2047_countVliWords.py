class Solution(object):
    def countValidWords(self, sentence):
        """
        :type sentence: str
        :rtype: int
        """
        def is_valid_word( word ) :
            if not word : 
                return False 
            
            for i , char in enumerate( word )  : 
                if char.isdigit():
                    return False 
                
                if char in '!.,' and i != len(word) - 1 : 
                    return False 
                
                if char == '-' : 
                    if word.count('-') > 1 or i == 0 or i == len(word) -1 : 
                        return False 
                    if not ( word[i-1].islower() and word[i+1].islower())  :
                        return False 
                    
            return True 
        
        return sum(1 for word in sentence.split() if is_valid_word(word))
