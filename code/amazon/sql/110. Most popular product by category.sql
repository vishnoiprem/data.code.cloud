CREATE TABLE products (
    product_id BIGINT PRIMARY KEY,
    category VARCHAR(100)
);


CREATE TABLE orders (
    order_id BIGINT PRIMARY KEY,
    product_id BIGINT,
    customer_id BIGINT,
    order_dt DATE,
    qty INTEGER,
    unit_price_usd FLOAT,
    channel VARCHAR(20)
);

INSERT INTO products (product_id, category) VALUES
(1001, 'Electronics'),
(1002, 'Books'),
(1003, 'Electronics'),
(1004, 'Clothing'),
(1005, 'Books');


INSERT INTO orders (order_id, product_id, customer_id, order_dt, qty, unit_price_usd, channel) VALUES
(1, 1001, 501, '2021-08-01', 10, 20.00, 'desktop'),
(2, 1002, 502, '2021-08-01', 5, 15.00, 'mobile'),
(3, 1003, 503, '2021-08-02', 7, 30.00, 'desktop'),
(4, 1004, 504, '2021-08-02', 8, 25.00, 'mobile'),
(5, 1005, 505, '2021-08-03', 6, 20.00, 'desktop'),
(6, 1001, 506, '2021-08-03', 12, 20.00, 'mobile'),
(7, 1003, 507, '2021-08-04', 10, 30.00, 'desktop'),
(8, 1005, 508, '2021-08-04', 7, 20.00, 'mobile');


WITH sales AS (
    SELECT
        p.category,
        o.product_id,
        SUM(o.qty) AS total_qty
    FROM
        orders o
    JOIN
        products p ON o.product_id = p.product_id
    GROUP BY
        p.category, o.product_id
),
ranked_sales AS (
    SELECT
        category,
        product_id,
        total_qty,
        RANK() OVER (PARTITION BY category ORDER BY total_qty DESC) AS rank
    FROM
        sales
)
SELECT
    category,
    product_id,
    total_qty
FROM
    ranked_sales
WHERE
    rank = 1;
