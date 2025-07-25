class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        count = 1 
        i = 0 
        while i< len( word ) - 1  :
            j = 1 
            while j < len( word )  and word[j] == word[i] : 
                j += 1 

            count *= j - i - 1 

            i = j 
        else : 
            i  += 1 

        return count 
