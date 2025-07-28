class Solution(object):
    def generateTag(self, caption):
        """
        :type caption: str
        :rtype: str
        """
        words = [ ''.join( c for c in word if c.isalpha() ) for word in caption.split()]
        words = [word for word in words if word ] 

        if not words : 
            return '#'
        

        result  = words[0].lower()

        for word in words[1: ] :
            if word : 
                result += word[0].upper() + word[1:].lower()

        result = '#' + result[:99]

        return result 
