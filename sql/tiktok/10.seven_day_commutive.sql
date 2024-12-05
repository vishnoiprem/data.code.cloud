-- Given a purchase table(user, purchase_time, amount_of_money, level1_category, level2_category), write a sql query to find the customer purchase in continue 7 days and with the total money greater than 500


CREATE TABLE purchases (
    user_id VARCHAR(50),
    purchase_time TIMESTAMP,
    amount_of_money DECIMAL(10, 2),
    level1_category VARCHAR(50),
    level2_category VARCHAR(50)
);

select *
from purchases;

INSERT INTO purchases (user_id, purchase_time, amount_of_money, level1_category, level2_category) VALUES
                                                                                                      ('user4', '2023-08-01 10:00:00', 10.00, 'grocery', 'fruits'),
('user4', '2023-08-02 11:00:00', 15.00, 'grocery', 'vegetables'),
('user4', '2023-08-03 12:00:00', 20.00, 'grocery', 'fruits'),
('user4', '2023-08-05 14:00:00', 30.00, 'grocery', 'fruits'),
('user4', '2023-08-06 15:00:00', 35.00, 'grocery', 'vegetables'),
('user4', '2023-08-07 16:00:00', 40.00, 'grocery', 'fruits');

('user1', '2023-08-01 10:00:00', 100.00, 'electronics', 'phones'),
('user1', '2023-08-02 11:00:00', 150.00, 'electronics', 'phones'),
('user1', '2023-08-03 12:00:00', 120.00, 'electronics', 'phones'),
('user1', '2023-08-04 13:00:00', 130.00, 'electronics', 'phones'),
('user1', '2023-08-05 14:00:00', 80.00, 'electronics', 'accessories'),
('user1', '2023-08-06 15:00:00', 140.00, 'electronics', 'phones'),
('user1', '2023-08-07 16:00:00', 160.00, 'electronics', 'phones'),
('user1', '2023-08-08 17:00:00', 200.00, 'electronics', 'phones'),

('user2', '2023-08-01 10:00:00', 50.00, 'clothing', 'mens'),
('user2', '2023-08-02 11:00:00', 60.00, 'clothing', 'mens'),
('user2', '2023-08-03 12:00:00', 70.00, 'clothing', 'mens'),
('user2', '2023-08-04 13:00:00', 40.00, 'clothing', 'womens'),
('user2', '2023-08-05 14:00:00', 50.00, 'clothing', 'womens'),
('user2', '2023-08-06 15:00:00', 30.00, 'clothing', 'womens'),
('user2', '2023-08-07 16:00:00', 20.00, 'clothing', 'mens'),
('user2', '2023-08-08 17:00:00', 80.00, 'clothing', 'womens'),

('user3', '2023-08-01 10:00:00', 10.00, 'grocery', 'fruits'),
('user3', '2023-08-02 11:00:00', 15.00, 'grocery', 'vegetables'),
('user3', '2023-08-03 12:00:00', 20.00, 'grocery', 'fruits'),
('user3', '2023-08-04 13:00:00', 25.00, 'grocery', 'vegetables'),
('user3', '2023-08-05 14:00:00', 30.00, 'grocery', 'fruits'),
('user3', '2023-08-06 15:00:00', 35.00, 'grocery', 'vegetables'),
('user3', '2023-08-07 16:00:00', 40.00, 'grocery', 'fruits');






  SELECT
        user_id,
        purchase_time::DATE AS purchase_date, -- Convert timestamp to date
        amount_of_money,
        SUM(amount_of_money) OVER (PARTITION BY user_id ORDER BY purchase_time::DATE ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS total_7_day_spending,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY purchase_time::DATE) AS rn
    FROM
        purchases
  ;



WITH user_purchases AS (
    SELECT
        user_id,
        purchase_time::DATE AS purchase_date, -- Convert timestamp to date
        amount_of_money,
        SUM(amount_of_money) OVER (PARTITION BY user_id ORDER BY purchase_time::DATE ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS total_7_day_spending,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY purchase_time::DATE) AS rn
    FROM
        purchases
),
consecutive_purchases AS (
    SELECT
        user_id,
        purchase_date,
        total_7_day_spending,
        rn,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY purchase_date) as cur_rn,
        purchase_date - INTERVAL '1 day' ,

        purchase_date - INTERVAL '1 day' * (rn - ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY purchase_date)) AS grp
    FROM
        user_purchases
)
select * from consecutive_purchases;



WITH user_purchases AS (
    SELECT 
        user_id,
        purchase_time::DATE AS purchase_date, -- Convert timestamp to date
        amount_of_money,
        SUM(amount_of_money) OVER (PARTITION BY user_id ORDER BY purchase_time::DATE ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS total_7_day_spending,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY purchase_time::DATE) AS rn
    FROM 
        purchases
),
consecutive_purchases AS (
    SELECT 
        user_id,
        purchase_date,
        total_7_day_spending,
        purchase_date - INTERVAL '1 day' * (rn - ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY purchase_date)) AS grp
    FROM 
        user_purchases
),
grouped_purchases AS (SELECT user_id,
                             COUNT(DISTINCT purchase_date) AS consecutive_days,
                             MAX(total_7_day_spending)     AS total_spending
                      FROM consecutive_purchases
                      GROUP BY user_id
--     HAVING
--         COUNT(DISTINCT purchase_date) = 7 AND
--         MAX(total_spending) > 500
-- )
)
select *
from grouped_purchases;


