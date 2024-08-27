-- # Q.32 Sometimes, payment transactions are repeated by accident; it could be due to user error, API failure or a retry error that causes a credit card to be charged twice.
-- #
-- # Using the transactions table, identify any payments made at the same merchant with the same credit card for the same amount within 10 minutes of each other. Count such repeated payments.
-- #
-- # Assumptions:
-- #
-- #   - The first transaction of such payments should not be counted as a repeated payment. This means, if there are two transactions performed by a merchant with the same credit card and for the same amount within 10 minutes, there will only be 1 repeated payment.
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    merchant_id INTEGER NOT NULL,
    credit_card VARCHAR(19) NOT NULL, -- Assuming credit card format 'XXXX-****-XXXX-XXXX'
    amount NUMERIC(10, 2) NOT NULL,
    transaction_time TIMESTAMP NOT NULL
);

INSERT INTO transactions (merchant_id, credit_card, amount, transaction_time) VALUES
(101, '1234-****-5678', 50.00, '2024-07-01 10:00:00'),
(101, '1234-****-5678', 50.00, '2024-07-01 10:05:00'),
(102, '5678-****-1234', 100.00, '2024-07-01 11:00:00'),
(101, '1234-****-5678', 50.00, '2024-07-01 10:20:00'),
(103, '9876-****-5432', 75.00, '2024-07-01 12:00:00'),
(103, '9876-****-5432', 75.00, '2024-07-01 12:07:00'),
(101, '1234-****-5678', 50.00, '2024-07-01 10:08:00');


select * from transactions;

with  data_txn as (select *,
                          lag(transaction_time) over (partition by credit_card,amount order by transaction_time asc ) as leg
                   from transactions)
select * from data_txn where  leg not null
