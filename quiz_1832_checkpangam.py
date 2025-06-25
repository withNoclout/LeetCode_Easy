class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        unique = set( char for char in sentence.lower() if char.isalpha() )

        return len(unique) == 26 
