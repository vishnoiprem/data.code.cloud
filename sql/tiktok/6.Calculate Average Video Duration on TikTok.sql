-- SQL Question 6: Calculate Average Video Duration on TikTok
-- On TikTok, each user can post several videos. For business decisions, it's often necessary to know the average duration of these videos to better understand the user engagement. For instance, if the average video duration is short, it could indicate that users on the platform prefer shorter, more concise content. Alternatively, longer average video lengths could infer that users enjoy or are more engaged with longer-form content. Calculate the average video duration for each TikTok user using the provided database tables.
--
-- Provided below is a snapshot of your 'users' table and 'videos' table:
-- #https://datalemur.com/blog/tiktok-sql-interview-questions

SELECT
    u.username,
    AVG(v.video_length_seconds) AS average_video_duration_seconds
FROM
    videos v
JOIN
    users u
ON
    v.user_id = u.user_id
GROUP BY
    u.username;