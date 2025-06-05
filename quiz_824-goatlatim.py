class Solution: 
    def toGoatLatin( self, sentence ) :
        vowels = set('aeiouAEIOU')
        words = sentence.split()
        result = []

        for i , word in enumerate( words ) :
            if word[0] in vowels : 
                new_word = word + "ma"
            else : 
                new_word = word[1:] + word[0] + "ma"

            new_word += 'a' * ( i + 1 )
            result.append(new_word)

        return ' '.join(result)
    
    
