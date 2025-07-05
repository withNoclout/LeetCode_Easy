class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def to_day( date ) :
            month , day = map( int , date.split('-'))
            return sum(days_in_month[:month -1 ]) + day 
        
        arrive_a = to_day( arriveAlice ) 
        leave_a = to_day( leaveAlice )
        arrive_b  = to_day( arriveBob ) 
        leave_b = to_day( leaveBob ) 

        start = max( arrive_a , arrive_b ) 
        end = min( leave_a , leave_b ) 


        return max( 0 , end - start + 1 )
