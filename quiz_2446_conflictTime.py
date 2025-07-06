class Solution(object):
    def haveConflict(self, event1, event2):
        """
        :type event1: List[str]
        :type event2: List[str]
        :rtype: bool
        """
        def to_minute( time_str) : 
            hours , minutes = map( int , time_str.split(':'))

            return hours * 60 + minutes 
        
        start1 = to_minutes(event1[0])
        end1 = to_minutes(event1[1])
        start2 = to_minutes(event2[0])
        end2 = to_minutes(event2[1])
        
        # Check if one event starts before another ends
        return start1 <= end2 and start2 <= end1
