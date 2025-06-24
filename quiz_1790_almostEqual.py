class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2 :
            return True 
        
        diff = [ (a,b) for a ,b in zip( s1, s2) if a != b ]

        return len(diff ) == 2 and diff[0] == diff[1][::-1]
