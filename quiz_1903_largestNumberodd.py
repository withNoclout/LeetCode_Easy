class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        # total = 0 
        # for i in range( len(num)): 
        #     number = ''.join(_ for _ in num[i:len(num)])
        #     if int(number) % 2 == 1 : 
        #         total = number 

        # return number

        for i in range( len(num) -1 , -1 , -1 ) : 
            if int(num[i] ) % 2 == 1 :
                return num[:i+1]
            
        return "" 
