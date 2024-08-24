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

