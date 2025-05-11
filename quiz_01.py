class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        new_num = ''
        for i ,num in enumerate(str(x)):
            print( i ,  str(x)[i] ,  str(x)[::-1])
            if str(x)[i] ==str(x)[::-1]:
                print( str(x)[i] ,  str(x)[::-1])
                new_num += str(x)[i]
        return print( "this is new number " + new_num) 
    
print(Solution().isPalindrome(123))
