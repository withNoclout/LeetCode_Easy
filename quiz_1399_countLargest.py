class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        group = {}
        for num in range( 1 , n + 1 ) :
            digit_sum  = sum( int(d) for d in str(num))
            group[digit_sum]  = group.get(digit_sum ,  0 ) + 1 

        max_size = max( group.values()) 

        return sum( 1 for size in group.values() if size == max_size ) 
