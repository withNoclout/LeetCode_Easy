class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2) if len(salary) > 2 else 0.0
