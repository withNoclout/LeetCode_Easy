class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer =  [] 
        for num in nums : 
            digits = str(num) 

            for digit in digits : 
                answer.append(int(digit))

        return answer 
