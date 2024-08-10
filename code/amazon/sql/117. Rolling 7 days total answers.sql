CREATE TABLE answers (
    answer_id BIGINT PRIMARY KEY,
    answer_date DATE,
    user_id BIGINT,
    question_id BIGINT
);



INSERT INTO answers (answer_id, answer_date, user_id, question_id) VALUES
(1, '2023-01-01', 101, 201),
(2, '2023-01-02', 102, 202),
(3, '2023-01-03', 103, 203),
(4, '2023-01-04', 104, 204),
(5, '2023-01-05', 105, 205),
(6, '2023-01-06', 106, 206),
(7, '2023-01-07', 107, 207),
(8, '2023-01-08', 108, 208),
(9, '2023-01-09', 109, 209),
(10, '2023-01-10', 110, 210);


SELECT
    answer_date,
    SUM(count) OVER (
        ORDER BY answer_date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS rolling_7_day_total
FROM (
    SELECT
        answer_date,
        COUNT(answer_id) AS count
    FROM
        answers
    GROUP BY
        answer_date
) AS daily_counts
ORDER BY
    answer_date;
