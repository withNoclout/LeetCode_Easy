class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        while len(s)  % k != 0 :
            s += fill 

        result = [] 

        for i in range( 0 , len(s) , k ) :
            result.append(s[i:i+k])

        return result
