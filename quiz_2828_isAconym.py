class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        if len(words) !=  len(s) :
            return False 
        
        aco = ''.join( word[0] for word in words ) 
        return aco == s 
