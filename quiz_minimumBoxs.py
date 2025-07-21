class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        total_apples = sum(apple) 
        capacity.sort(reversed = True ) 

        used_capacity = 0 

        for i , cap in enumerate( capacity ) : 
            used_capacity += cap 
            if used_capacity >= total_apples : 
                return i + 1 
        return len(capacity )
