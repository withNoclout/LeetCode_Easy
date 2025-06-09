class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        answer = [] 
        curr_num =  0

        for bit in nums : 
            curr_num = ( curr_num * 2 + bit ) % 5 

            answer.append(curr_num == 0)

        return answer
