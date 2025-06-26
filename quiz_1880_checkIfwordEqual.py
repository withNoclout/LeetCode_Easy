class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        def get_num( word ) : 
            return int( ''.join(str(ord(c) - ord('a') ) for c in word ))
        
        return get_num( firstWord ) + get_num( secondWord) == get_num(targetWord)
