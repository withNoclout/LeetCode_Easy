class Solution : 
    def mostCommanWord( self , words ) :
        banned = set( word.lower() for word in banned ) 
        for c in "!?',;." :
            words = words.replace( c , " " )

        freq = {} 
        for word in paragraph.lower().split() :
            if word not in banned :
                freq[word] = freq.get(word, 0) + 1

        max_count = 0 
        result = '' 
        for word , count  in freq.items() :
            if count > max_count :
                max_count = count 
                result = word   

        return result
