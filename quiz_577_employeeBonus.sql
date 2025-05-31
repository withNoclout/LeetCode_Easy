SELECT 
e.name , 
b.bonus 
FROM Emloyee e 
JOIN Bonus b 
ON e.empId = b.empId
WHERE b.bonus < 1000 or b.bonus IS NULL ;
