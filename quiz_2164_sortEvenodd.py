class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums ) 
        even_indices = [ nums[i] for i in range(0 , n , 2 ) ]
        odd_indices = [ nums[i] for i in range(1 , n , 2 ) ] 

        even_indices.sort()

        odd_indices.sort(reverse=True )

        result = []
        even_idk = odd_idk =  0 
        for i in range(n)  :
            if i % 2 == 0 :
                result.append(even_indices[even_idk])
                even_idk += 1 
            else : 
                result.append(odd_indices[odd_idk])
                odd_idk += 1 

        return result
