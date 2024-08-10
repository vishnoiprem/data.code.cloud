
WITH revenue_changes AS (
    SELECT
        revenue_date,
        revenue,
        LAG(revenue) OVER (ORDER BY revenue_date) AS prev_revenue
    FROM
        daily_revenue
)
SELECT
    revenue_date,
    revenue,
    prev_revenue,
    (revenue - prev_revenue) / prev_revenue * 100 AS dod_change_rate
FROM
    revenue_changes
WHERE
    prev_revenue IS NOT NULL
ORDER BY
    revenue_date;
