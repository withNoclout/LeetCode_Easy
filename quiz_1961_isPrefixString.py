class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        concat = '' 
        for word in words : 
            concat += word 
            if concat == s : 
                return True 
            if len(concat ) > len(s) or not s.startswith(concat) : 
                return False 
            
        return False 
