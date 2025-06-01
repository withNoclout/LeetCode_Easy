SELECT MAX(num ) as num 
FROM (
    SELECT num 
    FROM Mynumbers 
    GROUP BY num 
    HAVING CouNT(*) = 1 

)as singles ; 
