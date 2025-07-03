class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = [] 

        for word in words : 
            sorted_word = ''.join(sorted(word))

            if not result or sorted_word != ''.join(sorted(result[-1])) :
                result.append(word)

        return result 
