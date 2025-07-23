class Solution:
    def minChanges( self , n , k ) :
        if n < k or (n & k ) != k :
            return -1 
        return bin( n ^ k ).count('1')
