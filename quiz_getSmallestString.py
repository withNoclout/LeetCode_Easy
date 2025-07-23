class Solution(object):
    def getSmallestString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s )
        n = len(s) 

        for i in range(n-1  ) :
            if int(s_list[i] ) %2 == int( s_list[i+1] ) %2  : 
                s_list[i] , s_list[i+1 ] = s_list[i+1] , s_list[i] 
                new_s = ''.join(s_list ) 
                if new_s < s :
                    return new_s 
                
                s_list[i] , s_list[i+1]  = s_list[i+1 ] , s_list[i] 

        return s 
