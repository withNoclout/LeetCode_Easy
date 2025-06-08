class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        n = len(s )
        perm = [] 
        low , high = 0 , n 

        for char in s : 
            if char == 'I' : 
                perm.append(low ) 
                low += 1 
            else : 
                perm.append( high ) 
                high -= 1 

        perm.append(low)  # or high, both will be the same at this point

        return  perm
