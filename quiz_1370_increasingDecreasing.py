class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = [ 0 ] * 26 
        for char in s : 
            freq[ ord(char )  - ord( 'a' ) ] += 1 

        result = [] 

        while len(result)  < len(s ) :
            for i in range(26) :
                if freq[i] > 0 :
                    result.append( chr( i + ord('a') )) 
                    freq[i] -= 1 

            for i in range( 25 , -1 , - 1 ) :
                if freq[i ] > 0 : 
                    result.append(chr( i + ord('a')))
                    ferq[i] -= 1 

        return ''.join(result)
