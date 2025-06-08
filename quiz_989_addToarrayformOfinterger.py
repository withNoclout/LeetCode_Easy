class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        result  = [] 
        carry =  0 
        i = len(num ) -  1 

        while i >= 0 or k > 0 or carry : 
            digit = num[i] if i >= 0 else 0 

            k_digit =  k % 10 if k > 0 else 0 
            total = digit + k_digit + carry 
            carry = total // 10 
            result.append( total % 10 ) 

            i -= 1 
            k //= 10 

        return result[::-1 ] 
    
    
