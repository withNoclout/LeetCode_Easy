class Solution(object):
    def countTime(self, time):
        """
        :type time: str
        :rtype: int
        """
        hours , minutes = time[:2] , time[3:]

        valid_hours = 1 
        valid_minutes = 1

        if hours == '??' :
            valid_hours = 24 
        elif hours[0] == '?' :
            valid_hours = 3 if hours[1] <= '3' else 2 
        elif hours[1] == '?' :
            valid_hours = 4 if hours[0] =='2'  else 10 

        if minuts == '??' :
            valid_minutes = 60 
        elif minutes[0] == '?' :
            valid_minutes = 6  
        elif minutes[1] == '?' :
            valid_minutes = 10 

        return valid_hours * valid_minutes 
