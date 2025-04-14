-- Create the emails table



-- Create the emails table
CREATE TABLE emails1 (
    email_id INT PRIMARY KEY,
    user_id INT,
    signup_date TIMESTAMP
);

-- Create the texts table
CREATE TABLE texts1 (
    text_id INT PRIMARY KEY,
    email_id INT REFERENCES emails(email_id),
    signup_action VARCHAR(50),
    action_date TIMESTAMP
);

-- Insert sample data into the emails table
INSERT INTO emails1 (email_id, user_id, signup_date)
VALUES
(125, 7771, '2022-06-14 00:00:00'),
(433, 1052, '2022-07-09 00:00:00');

-- Insert sample data into the texts table
INSERT INTO texts1 (text_id, email_id, signup_action, action_date)
VALUES
(6878, 125, 'Confirmed', '2022-06-14 00:00:00'),
(6997, 433, 'Not Confirmed', '2022-07-09 00:00:00'),
(7000, 433, 'Confirmed', '2022-07-10 00:00:00');



select * from emails1 as e
left join public.texts1 e2 on e.email_id = e2.email_id
where e.signup_date = e2.action_date - INTERVAL '1 day'