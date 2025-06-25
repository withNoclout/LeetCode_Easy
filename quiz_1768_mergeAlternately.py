class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # result = [] 
        # for i in range(max( word1 , word2 ) ) :
        #     if i <= len(word1 ) : 
        #         result.append(word1) 
        #     if i <= len( word2) :
        #         result.append(word2)

        # return result

        merge = [] 
        i = 0 
        while i < len(word1) or i < len(word2 ) :
            if i < len(word1 ) :
                merge.append( word1[i])
            if i < len(word2) :
                merge.append(word2[i] )
            i+=1 

        return ''.join(merge)
