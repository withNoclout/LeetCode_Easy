class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0 
        for a in range(1 , n+ 1 ) :
            for b in range( a , n+ 1 ) : 
                c_s  = a * a + b *b 
                c = int(c_s ** 0.5 )
                if c <= n and c*c == c_s : 
                    count += 2 if a != b else 1 
        return count  
