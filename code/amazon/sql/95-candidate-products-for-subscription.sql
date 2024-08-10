CREATE TABLE orders_3 (
    order_id BIGINT,
    product_id BIGINT,
    customer_id BIGINT,
    order_dt DATE,
    qty INTEGER,
    unit_price_usd FLOAT,
    channel VARCHAR(20) -- mobile, desktop
);



INSERT INTO orders_3 (order_id, product_id, customer_id, order_dt, qty, unit_price_usd, channel) VALUES
(1, 1001, 501, '2023-01-01', 2, 20.0, 'mobile'),
(2, 1002, 502, '2023-01-05', 1, 15.0, 'desktop'),
(3, 1001, 503, '2023-01-07', 3, 20.0, 'mobile'),
(4, 1003, 504, '2023-01-10', 1, 25.0, 'desktop'),
(5, 1002, 505, '2023-01-15', 2, 15.0, 'mobile'),
(6, 1004, 506, '2023-01-20', 1, 30.0, 'desktop'),
(7, 1001, 507, '2023-01-22', 4, 20.0, 'mobile'),
(8, 1003, 508, '2023-01-25', 2, 25.0, 'desktop'),
(9, 1004, 509, '2023-01-28', 1, 30.0, 'mobile'),
(10, 1005, 510, '2023-01-30', 3, 10.0, 'desktop');






select * from orders_3



WITH order_counts AS (
    SELECT
        product_id,
        COUNT(DISTINCT customer_id) AS unique_customers,
        COUNT(*) AS order_count
    FROM
        orders_3
    WHERE
        order_dt >= '2023-01-01' AND order_dt <= '2023-01-31'
    GROUP BY
        product_id
)
SELECT
    product_id
FROM
    order_counts
WHERE
    order_count > 1 -- Products ordered more than once in the given period
    AND unique_customers > 1 -- Products ordered by more than one customer
ORDER BY
    order_count DESC, unique_customers DESC;
