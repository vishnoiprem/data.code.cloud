


CREATE TABLE user_actions (
    action_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    action_type VARCHAR(50) NOT NULL, -- Example: 'sign-in', 'like', 'comment'
    action_date DATE NOT NULL
);