CREATE TABLE answers3 (
    answer_id BIGINT PRIMARY KEY,
    answer_date DATE,
    user_id BIGINT,
    question_id BIGINT,
    device VARCHAR(50) -- e.g., 'mobile', 'desktop'
);


INSERT INTO answers3 (answer_id, answer_date, user_id, question_id, device) VALUES
(1, '2023-01-01', 101, 201, 'mobile'),
(2, '2023-01-01', 102, 202, 'desktop'),
(3, '2023-01-02', 103, 203, 'mobile'),
(4, '2023-01-02', 104, 204, 'desktop'),
(5, '2023-01-02', 105, 205, 'mobile'),
(6, '2023-01-03', 106, 206, 'desktop'),
(7, '2023-01-03', 107, 207, 'mobile'),
(8, '2023-01-03', 108, 208, 'mobile'),
(9, '2023-01-04', 109, 209, 'desktop'),
(10, '2023-01-04', 110, 210, 'desktop');


WITH daily_counts AS (
    SELECT
        answer_date,
        device,
        COUNT(answer_id) AS answer_count
    FROM
        answers3
    GROUP BY
        answer_date, device
),
ranked_days AS (
    SELECT
        answer_date,
        device,
        answer_count,
        RANK() OVER (PARTITION BY device ORDER BY answer_count DESC) AS rank
    FROM
        daily_counts
)
SELECT
    answer_date,
    device,
    answer_count
FROM
    ranked_days
WHERE
    rank = 1
ORDER BY
    device, answer_date;
