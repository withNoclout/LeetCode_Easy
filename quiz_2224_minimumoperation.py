class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        def to_min( time_str  ) : 
            hours, minutes = map( int , time_str.split(':'))
            return hours * 60 + minutes 
        
        current_minutes = to_min( current )
        correct_minutes = to_min( correct )

        diff  = correct_minutes - current_minutes

        operations = 0 
        increments = [60 , 15 , 5 ,1 ]

        for increment in increments : 
            operations += diff // increment 
            diff %= increments 

        return operations 
    
