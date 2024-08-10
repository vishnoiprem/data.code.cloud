CREATE TABLE Device_table (
    device_id BIGINT PRIMARY KEY,
    device_name VARCHAR(50)
);


CREATE TABLE Purchase_table (
    purchase_id BIGINT PRIMARY KEY,
    cust_id BIGINT,
    device_id BIGINT,
    purchase_date DATE
);

INSERT INTO Device_table (device_id, device_name) VALUES
(1, 'iphone'),
(2, 'ipad'),
(3, 'android'),
(4, 'laptop');



INSERT INTO Purchase_table (purchase_id, cust_id, device_id, purchase_date) VALUES
(101, 201, 1, '2023-01-01'), -- customer 201 bought an iphone
(102, 202, 2, '2023-01-05'), -- customer 202 bought an ipad
(103, 201, 3, '2023-02-01'), -- customer 201 bought an android
(104, 203, 1, '2023-02-15'), -- customer 203 bought an iphone
(105, 204, 2, '2023-03-01'), -- customer 204 bought an ipad
(106, 205, 1, '2023-03-10'), -- customer 205 bought an iphone
(107, 202, 1, '2023-03-15'), -- customer 202 bought an iphone
(108, 206, 3, '2023-03-20'), -- customer 206 bought an android
(109, 207, 1, '2023-04-01'), -- customer 207 bought an iphone
(110, 208, 4, '2023-04-10'); -- customer 208 bought a laptop

-- #Q1: Customer who bought iPhone but never bought iPad
SELECT DISTINCT p1.cust_id
FROM Purchase_table p1
JOIN Device_table d1 ON p1.device_id = d1.device_id
WHERE d1.device_name = 'iphone'
  AND p1.cust_id NOT IN (
      SELECT p2.cust_id
      FROM Purchase_table p2
      JOIN Device_table d2 ON p2.device_id = d2.device_id
      WHERE d2.device_name = 'ipad'
  );

201
203
205
207


with  cust_data as (select cust_id
                         , MAX(case when device_name = 'iphone' then 1 else 0 end) is_iphone

                         , max(case when device_name = 'ipad' then 1 else 0 end)   is_ipad
                    from Purchase_table as p1
                             JOIN Device_table d1 ON p1.device_id = d1.device_id
                    GROUP BY cust_id)
select *
from cust_data
where is_iphone =1 AND is_ipad=0

201
203
205
207


201
203
205
207



SELECT DISTINCT p1.cust_id
FROM Purchase_table p1
JOIN Device_table d1 ON p1.device_id = d1.device_id
WHERE d1.device_name = 'iphone'
  AND p1.cust_id NOT IN (
      SELECT p2.cust_id
      FROM Purchase_table p2
      JOIN Device_table d2 ON p2.device_id = d2.device_id
      WHERE d2.device_name = 'ipad'
        AND p2.purchase_date < p1.purchase_date
  );