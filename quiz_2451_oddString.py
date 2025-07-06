class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def get_diff_array(word ) :
            return tuple( ord(word[i+1] - ord(word[i]) for i in range( len(word ))))
        
        diff_array = [ get_diff_array(word) for word in words ] 

        for i , diff in enumerate(diff_array) :
            if diff_array.count(diff) == 1  : 
                return words[i]
            
        return "" 
