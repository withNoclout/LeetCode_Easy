class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        s =str(n) 
        if len(s )<= 3 : 
            return s 
        
        res = []

        count = 0 
        for i in range( len(s ) -1 , -1 ,-1 ) : 
            res.append(s[i] )
            count += 1 
            if count % 3 == 0 and i != 0:
                res.append('.')

        return ''.join(res[::-1])  # Reverse the list and join to form the final string
