class Solution(object):
    def hardestWorker(self, n, logs):
        """
        :type n: int
        :type logs: List[List[int]]
        :rtype: int
        """
        max_time = 0 
        max_id = n 
        prev_time = 0 

        for emp_id , leave_time in logs  :
            duration = leave_time - prev_time 

            if duration > max_time or( duration == max_time  and emp_id < max_id ):
                max_time = duration 
                max_id = emp_id

            prev_time = leave_time 

        return max_id 
