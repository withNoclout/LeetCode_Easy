class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        connt = 0 
        for i in range( len(words) ) :
            for j in range( i +1  , len(words ) ) :
                str1 , str2  = words[i] , words[j]
                if len(str1) <= len(str2 ) and str2.startwith(str1) and str2.endswith(str1) :
                    connt += 1
        return connt
