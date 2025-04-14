-- SQL Question 2: Identify TikTok's Most Active Users
-- Create the Users table
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    username VARCHAR(255),
    signup_date DATE
);

-- Insert sample data into Users table
INSERT INTO Users (user_id, username, signup_date)
VALUES
(1, 'user1', '2020-01-01'),
(2, 'user2', '2020-02-02'),
(3, 'user3', '2020-05-05'),
(4, 'user4', '2020-12-12');

-- Create the Videos table
CREATE TABLE Videos (
    video_id INT PRIMARY KEY,
    user_id INT,
    upload_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Insert sample data into Videos table
INSERT INTO Videos (video_id, user_id, upload_date)
VALUES
(1001, 1, '2020-01-02'),
(1002, 1, '2020-01-03'),
(1003, 2, '2020-02-03'),
(1004, 3, '2020-03-03'),
(1005, 4, '2020-04-04'),
(1006, 4, '2020-05-04'),
(1007, 4, '2020-05-04'),
(1008, 4, '2020-05-04'),
(1009, 3, '2020-06-04'),
(1010, 2, '2020-07-07');

select user_id, count(*), max(upload_date)
from Videos
group by user_id;


select username,COUNT(*)
from users as u
left join Videos V on u.user_id = V.user_id
GROUP BY username
having count(*)>2
