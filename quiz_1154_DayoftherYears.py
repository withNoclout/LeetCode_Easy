class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year , month , day = map( int , date.split('-'))

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if year % 4 == 0 and ( year % 100 != 0 or year % 400 == 0 ) : 
            days_in_month[1] = 29 


        total_day = sum( days_in_month[ : month -1 ]) + day 
        return total_day 
