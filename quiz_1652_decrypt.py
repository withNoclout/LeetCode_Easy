class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        result = [0] * n

        if k == 0 :
            return result 
        
        for i in range(n)  :
            total = 0 
            if k > 0  : 
                for  j in range ( 1 , k +1 ):
                    total += code[(i+j) % n ]

            else : 
                for j in range( 1 , -k +1  ) : 
                    total += code[(i-j + n ) % n ]
            result[i] = total 

        return result 
