class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        words = sentence.split()

        if not words :
            return True
        
        for i in range( len(words) ) :
            curr_last = words[i][-1]
            next_first = words[(i+1) % len(words)][0]
            if curr_last != next_first : 
                return False 
            
        return True
