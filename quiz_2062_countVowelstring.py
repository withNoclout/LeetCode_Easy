class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        # vowel = 'aeiou'.split()
        # count = 0 
        # for k in word : 
        #     if k in vowel : 
        #         count += 1 

        # return count 

        vowels= set('aeiou')
        count = 0 
        for i in range( len(word ))  :
            freq = {}
            for j in range( i , len( word ) ) :
                if word[j] not in vowels :
                    break 
                freq[word[j]] = freq.get(word[j] , 0) + 1 
                if len(freq) == 5 : 
                    count += 1 
        return count 
