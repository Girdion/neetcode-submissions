WITH rankings AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY student_id
    ORDER BY score DESC, exam_id ASC) AS rnk
    FROM exam_results
)

SELECT student_id, exam_id, score
FROM rankings
WHERE rnk = 1;