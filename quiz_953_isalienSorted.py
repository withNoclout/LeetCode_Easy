class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        char_map = {c : i for i , c in enumerate(order)}

        for i in range( len(words ) - 1 ) : 
            word1 , word2 =  words[i]  , words[i+1 ] 

            for j in range(len(word1 )) : 
                if j >= len(word2)  : 
                    return False 

            if word1[j] != word2[j]  :
                if char_map[word1[j]] > char_map[word2[j]] :
                    return False 
                break
        return True 
     
