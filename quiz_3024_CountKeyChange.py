class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s ) <= 1 :
            return 0
        count = 0 
        s = s.lower()

        for i in range( 1,  len(s)  ) :
            if s[i] != s[i-1] :
                count+= 1 

        return count 
