-- https://datalemur.com/questions/signup-confirmation-rate


-- Create the emails table
CREATE TABLE emails (
    email_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    signup_date TIMESTAMP
);

-- Insert data into the emails table
INSERT INTO emails (email_id, user_id, signup_date) VALUES
(125, 7771, '2022-06-14 00:00:00'),
(236, 6950, '2022-07-01 00:00:00'),
(433, 1052, '2022-07-09 00:00:00');

-- Create the texts table
CREATE TABLE texts (
    text_id INTEGER PRIMARY KEY,
    email_id INTEGER REFERENCES emails(email_id),
    signup_action VARCHAR(50)
);

-- Insert data into the texts table
INSERT INTO texts (text_id, email_id, signup_action) VALUES
(6878, 125, 'Confirmed'),
(6920, 236, 'Not Confirmed'),
(6994, 236, 'Confirmed');

select 1.00*COUNT( distinct case  when signup_action='Confirmed'  then  e.email_id else null end  )/COUNT(e.email_id )
from emails as e
INNER join texts t on e.email_id = t.email_id
;