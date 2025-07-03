class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        # num_str = str(num)
        # count = 0 

        # for i in range(len(num_str) - k + 1 ): 
        #     substring = int(num_str[i:i+k])
        #     if substring != 0 and num % substring == 0 : 
        #         count + 1 


        # return count 

        num_str = str(num)
        count = 0 

        for i in range(len(num_str) - k + 1 ) :
            substring = num_str[i:i+k]
            sub_num = int(substring)

            if sub_num == 0 :
                continue 

            if num % sub_num == 0 :
                count += 1 

        return count 
