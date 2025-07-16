class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        def isSym( num ) : 
            s = str(num ) 
            n = len(s) 
            if n % 2 != 0 :
                return False 
            half = n // 2 
            first_half_sum = sum( int(d for d in s[:half]))
            seconde_half = sum( int(d) for d in s[half:])

            return first_half_sum == seconde_half 
        
        count = 0 

        for num in range( low , high + 1 ) :
            if isSym( num ) :
                count += 1 

        return count 
    
# ============== genius way to solve he store as local ==================


li = []
n = []
for i in range(0, 10001):
        no = str(i)
        if len(no) % 2 != 0:
            continue
        half = int(len(no)/2)
        if sum([int(j) for j in no[:half]]) == sum([int(j) for j in no[half:]]):
            li.append(i)
            n.append(len(li))

class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        import bisect

        i1 = bisect.bisect_left(li, low)
        i2 = bisect.bisect_left(li, high+1)
        return i2 - i1

            
                    

        
