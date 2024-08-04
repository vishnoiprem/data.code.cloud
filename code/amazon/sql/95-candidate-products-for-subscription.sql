


CREATE TABLE orders_94 (
    order_id BIGINT,
    product_id BIGINT,
    customer_id BIGINT,
    order_dt DATE,
    qty INTEGER,
    unit_price_usd FLOAT,
    channel VARCHAR(20) -- mobile, desktop
);


INSERT INTO orders_94 (order_id, product_id, customer_id, order_dt, qty, unit_price_usd, channel) VALUES
(1, 10000045, 1, '2021-08-01', 5, 10.0, 'mobile'),
(2, 10000045, 2, '2021-08-02', 3, 10.0, 'desktop'),
(3, 10000060, 3, '2021-08-03', 2, 15.0, 'mobile'),
(4, 10000060, 4, '2021-08-04', 7, 15.0, 'desktop'),
(5, 10000067, 5, '2021-08-05', 1, 20.0, 'mobile'),
(6, 10000067, 6, '2021-08-06', 10, 20.0, 'desktop'),
(7, 10000089, 7, '2021-08-07', 4, 5.0, 'mobile'),
(8, 10000036, 8, '2021-08-08', 6, 5.0, 'desktop'),
(9, 10000065, 9, '2021-08-09', 8, 2.0, 'mobile'),
(10, 10000065, 10, '2021-08-10', 3, 2.0, 'desktop'),
(11, 10000045, 11, '2021-08-11', 2, 10.0, 'mobile'),
(12, 10000060, 12, '2021-08-12', 5, 15.0, 'desktop'),
(13, 10000067, 13, '2021-08-13', 7, 20.0, 'mobile'),
(14, 10000089, 14, '2021-08-14', 6, 5.0, 'desktop'),
(15, 10000036, 15, '2021-08-15', 9, 5.0, 'mobile'),
(16, 10000065, 16, '2021-08-16', 10, 2.0, 'desktop'),
(17, 10000045, 17, '2021-08-17', 8, 10.0, 'mobile'),
(18, 10000060, 18, '2021-08-18', 6, 15.0, 'desktop'),
(19, 10000067, 19, '2021-08-19', 4, 20.0, 'mobile'),
(20, 10000089, 20, '2021-08-20', 3, 5.0, 'desktop'),
(21, 10000036, 21, '2021-08-21', 2, 5.0, 'mobile'),
(22, 10000065, 22, '2021-08-22', 1, 2.0, 'desktop');










WITH product_sales AS (
    SELECT
        product_id,
        SUM(unit_price_usd * qty) AS total_sales
    FROM
        orders_94
    WHERE
        order_dt >= '2021-08-01' AND order_dt < '2021-09-01'
    GROUP BY
        product_id
),
ranked_sales AS (
    SELECT
        product_id,
        total_sales,
        RANK() OVER (ORDER BY total_sales DESC) AS sales_rank_desc,
        RANK() OVER (ORDER BY total_sales ASC) AS sales_rank_asc
    FROM
        product_sales
)
SELECT
    product_id,
    CASE
        WHEN sales_rank_desc <= 3 THEN 'top'
        WHEN sales_rank_asc <= 3 THEN 'bottom'
    END AS category
FROM
    ranked_sales
WHERE
    sales_rank_desc <= 3 OR sales_rank_asc <= 3;
