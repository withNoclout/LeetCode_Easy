class Solution : 
    def splitWordsBySeparator( self, words, separator):
        result = []
        for word in words:
            split_words = word.split(separator)
            for split_word in split_words:
                if split_word:
                    result.append(split_word)
        return result
