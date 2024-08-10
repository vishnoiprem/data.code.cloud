CREATE TABLE orders_4 (
    order_id BIGINT,
    product_id BIGINT,
    customer_id BIGINT,
    order_dt DATE,
    qty INTEGER,
    unit_price_usd FLOAT,
    channel VARCHAR(20) -- mobile, desktop
);


INSERT INTO orders_4 (order_id, product_id, customer_id, order_dt, qty, unit_price_usd, channel) VALUES
(1, 1001, 501, '2023-01-01', 2, 20.0, 'mobile'),
(2, 1002, 502, '2023-01-05', 1, 15.0, 'desktop'),
(3, 1001, 503, '2023-01-07', 3, 20.0, 'mobile'),
(4, 1003, 504, '2023-01-10', 1, 25.0, 'desktop'),
(5, 1002, 505, '2023-01-15', 2, 15.0, 'mobile'),
(6, 1004, 506, '2023-01-20', 1, 30.0, 'desktop'),
(7, 1001, 507, '2023-01-22', 4, 20.0, 'mobile'),
(8, 1003, 508, '2023-01-25', 2, 25.0, 'desktop'),
(9, 1004, 509, '2023-01-28', 1, 30.0, 'mobile'),
(10, 1005, 510, '2023-01-30', 3, 10.0, 'desktop'),
(11, 1002, 501, '2023-02-01', 1, 15.0, 'mobile'),
(12, 1003, 502, '2023-02-05', 1, 25.0, 'desktop'),
(13, 1001, 503, '2023-02-07', 2, 20.0, 'mobile'),
(14, 1005, 504, '2023-02-10', 4, 10.0, 'desktop'),
(15, 1004, 505, '2023-02-15', 1, 30.0, 'mobile');


WITH customer_spending AS (
    SELECT
        customer_id,
        SUM(qty * unit_price_usd) AS total_spent
    FROM
        orders_4
    WHERE
        order_dt >= '2023-01-01' AND order_dt <= '2023-01-31'
    GROUP BY
        customer_id
)
SELECT
    customer_id
FROM
    customer_spending
WHERE
    total_spent > 100;
