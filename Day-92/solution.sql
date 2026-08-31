WITH valid_start AS (
    SELECT s1.id AS start_id
    FROM Stadium s1
    JOIN Stadium s2
        ON s2.id = s1.id + 1
    JOIN Stadium s3
        ON s3.id = s1.id + 2
    WHERE s1.people >= 100
      AND s2.people >= 100
      AND s3.people >= 100
)

SELECT DISTINCT s.*
FROM Stadium s
JOIN valid_start v
    ON s.id BETWEEN v.start_id AND v.start_id + 2
ORDER BY s.visit_date;
