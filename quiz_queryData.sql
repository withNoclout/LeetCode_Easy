SELECT 
    lb.book_id,
    lb.title,
    lb.author,
    lb.genre,
    lb.publication_year,
    COUNT(br.record_id) as current_borrowers
FROM 
    library_books lb
LEFT JOIN 
    borrowing_records br
ON 
    lb.book_id = br.book_id
    AND br.return_date IS NULL
GROUP BY 
    lb.book_id,
    lb.title,
    lb.author,
    lb.genre,
    lb.publication_year,
    lb.total_copies
HAVING 
    COUNT(br.record_id) = lb.total_copies
    AND COUNT(br.record_id) > 0
ORDER BY 
    current_borrowers DESC,
    lb.title ASC;
