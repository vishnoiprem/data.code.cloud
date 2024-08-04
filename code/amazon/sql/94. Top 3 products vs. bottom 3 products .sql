
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name TEXT NOT NULL
);

CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id),
    sale_date TIMESTAMP NOT NULL,
    quantity INTEGER NOT NULL
);



-- Inserting products
INSERT INTO products (product_name) VALUES
('Product A'),
('Product B'),
('Product C');

-- Inserting sales for the current month
INSERT INTO sales (product_id, sale_date, quantity) VALUES
(1, '2024-06-01 10:00:00', 2),
(1, '2024-06-02 11:00:00', 1),
(2, '2024-06-03 12:00:00', 4),
(2, '2024-06-04 13:00:00', 2),
(3, '2024-06-05 14:00:00', 3),
(1, '2024-06-06 15:00:00', 5),
(3, '2024-06-07 16:00:00', 1);

-- Inserting sales for previous months (to show filtering)
INSERT INTO sales (product_id, sale_date, quantity) VALUES
(1, '2024-05-01 10:00:00', 3),
(2, '2024-05-02 11:00:00', 2),
(3, '2024-05-03 12:00:00', 1);

select *
from sales;


select
    * from  sales as s
left join products p on p.product_id = s.product_id;


select
    p.product_name,
    date_trunc('month',sale_date) as sales_month,
    SUM(quantity) as quantity
from  sales as s
left join products p on p.product_id = s.product_id
-- where     DATE_TRUNC('month', s.sale_date) = DATE_TRUNC('month', CURRENT_DATE)

GROUP BY     p.product_name,date_trunc('month',sale_date)
