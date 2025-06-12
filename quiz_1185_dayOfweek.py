class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        days = [ 'Saturday' , 'Sunday' , 'Monday' , 'Tuesday' , 'Wednesday' ,  'Thursday' , 'Friday']

        if month < 3 : 
            month += 12 
            year -= 1 

        k = day 
        m = month 
        D = year % 100 
        C = year // 100 

        f = k + ((13 * (m + 1)) // 5) + D + (D // 4) + (C // 4) - (2 * C)

        day_index = f % 7 
        if day_index < 0 : 
            day_index += 7 

        return days[day_index] 
