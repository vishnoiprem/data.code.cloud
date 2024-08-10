CREATE TABLE daily_revenue (
    revenue_date DATE PRIMARY KEY,
    revenue DECIMAL(10, 2)
);

INSERT INTO daily_revenue (revenue_date, revenue) VALUES
('2023-01-01', 1000.00),
('2023-01-02', 1500.00),
('2023-01-03', 1200.00),
('2023-01-04', 1300.00),
('2023-01-05', 1700.00),
('2023-01-06', 1600.00),
('2023-01-07', 1800.00),
('2023-01-08', 2000.00),
('2023-01-09', 2200.00),
('2023-01-10', 2400.00);


SELECT
    revenue_date,
    revenue,
    AVG(revenue) OVER (
        ORDER BY revenue_date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS rolling_avg_revenue
FROM
    daily_revenue
ORDER BY
    revenue_date;
