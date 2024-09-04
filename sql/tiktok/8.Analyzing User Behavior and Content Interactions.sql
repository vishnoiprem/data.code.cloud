
-- Q.31 Assume you're given a table containing information on Facebook user actions. Write a query to obtain number of monthly active users (MAUs) in July 2022, including the month in numerical format "1, 2, 3".

CREATE TABLE user_actions (
    action_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    action_type VARCHAR(50) NOT NULL, -- Example: 'sign-in', 'like', 'comment'
    action_date DATE NOT NULL
);


INSERT INTO user_actions (user_id, action_type, action_date) VALUES
(1, 'sign-in', '2022-06-10'),
(1, 'like', '2022-07-05'),
(2, 'comment', '2022-06-15'),
(2, 'sign-in', '2022-07-05'),
(3, 'like', '2022-07-10'),
(3, 'comment', '2022-06-20'),
(4, 'sign-in', '2022-07-01'),
(4, 'like', '2022-07-25'),
(4, 'sign-in', '2022-06-15'),
(5, 'comment', '2022-07-15'),
(6, 'like', '2022-06-30'),
(6, 'comment', '2022-07-10');

SELECT
    Users.user_id,
    COUNT(Videos.video_id) AS total_videos,
    SUM(Videos.video_likes) AS total_likes
FROM
    Users
JOIN
    Videos ON Users.user_id=Videos.user_id
GROUP BY
    Users.user_id
ORDER BY
    total_likes DESC
LIMIT 5;



select user_id, extract(month from user_actions.action_date)

, lag(action_date) over (partition by  user_id order by action_date asc ))
from user_actions


with cte1 as
(select distinct user_id
from items_per_order
where extract(month from event_date) = 7
and extract(year from event_date) = 2022
intersect
select distinct user_id
from items_per_order
where extract(month from event_date) = 6
and extract(year from event_date) = 2022)

select '7' as month, count(user_id) as monthly_count
from cte1;

WITH june_actions AS (
    SELECT DISTINCT user_id
    FROM user_actions
    WHERE action_date BETWEEN '2022-06-01' AND '2022-06-30'
),
july_actions AS (
    SELECT DISTINCT user_id
    FROM user_actions
    WHERE action_date BETWEEN '2022-07-01' AND '2022-07-31'
)
SELECT COUNT(DISTINCT ja.user_id) AS mau_july_2022
FROM july_actions ja
JOIN june_actions ja2 ON ja.user_id = ja2.user_id;