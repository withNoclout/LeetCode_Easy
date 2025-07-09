class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        vowels = [ 'a' , 'e' , 'i' ,'o' , 'u' ] 
        count = 0 

        for i in range( left , right + 1 ) :
            if words[i] and words[i][0] in vowels and words[i][i-1] in vowels : 
                count += 1 

        return count 
