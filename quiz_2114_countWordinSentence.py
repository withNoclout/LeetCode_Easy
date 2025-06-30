class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        total  = 0 
        for word in sentences : 
            if len(word.split()) > total : 
                total = len(word.split())

        return total 
