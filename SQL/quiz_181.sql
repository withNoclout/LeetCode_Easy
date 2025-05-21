SELECT e.name AS employee 
FROM Employee e 
JOIN Employee m 
ON e.managerID =  m.id 
WHERE e.salary > m.salary ; 
