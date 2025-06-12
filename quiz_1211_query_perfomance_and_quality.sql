-- SELECT 
--     query_name , 
--     ROUND( AVG( CAST( rating AS FLOAT ) / position ) ,  2 ) AS quality , 
--     ROUND( 100.0 * SUM( CASE WHEN rating < 3 THEN 1 ELSE 0 END )  / COUNT(*) , 2 ) AS 
--     poor_query_percentage
-- FROM Queries 
-- GROUP BY query_name  ; 


SELECT 
    query_name,
    ROUND(AVG(CAST(rating AS DECIMAL(10,2)) / CAST(position AS DECIMAL(10,2))), 2) AS quality,
    ROUND(100.0 * SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / CAST(COUNT(*) AS DECIMAL(10,2)), 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;
