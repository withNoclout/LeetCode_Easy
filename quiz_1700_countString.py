class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        from collections import deque 

        students = deque(students)
        sandwiches = sandwiches[::-1]

        attempts = 0
        while sandwiches and attempts < len(students):
            if students[0] == sandwiches[ -1]:
                students.popleft()
                sandwiches.pop()
                attempts = 0
            else : 
                students.append(students.popleft())
                attempts += 1
        return len(students)	

