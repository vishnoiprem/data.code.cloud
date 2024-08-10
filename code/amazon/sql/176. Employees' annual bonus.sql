CREATE TABLE employees (
    employee_id BIGINT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    base_salary FLOAT
);

CREATE TABLE performance (
    employee_id BIGINT,
    year INT,
    rating INT, -- Rating from 1 to 5
    PRIMARY KEY (employee_id, year),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);


INSERT INTO employees (employee_id, name, department, base_salary) VALUES
(1, 'Alice', 'Engineering', 100000),
(2, 'Bob', 'Engineering', 95000),
(3, 'Charlie', 'HR', 85000),
(4, 'David', 'Marketing', 90000),
(5, 'Eve', 'Engineering', 105000);

INSERT INTO performance (employee_id, year, rating) VALUES
(1, 2023, 5),
(2, 2023, 3),
(3, 2023, 4),
(4, 2023, 2),
(5, 2023, 5);


SELECT
    e.employee_id,
    e.name,
    e.department,
    e.base_salary,
    p.year,
    p.rating,
    CASE
        WHEN p.rating = 5 THEN e.base_salary * 0.20
        WHEN p.rating = 4 THEN e.base_salary * 0.15
        WHEN p.rating = 3 THEN e.base_salary * 0.10
        WHEN p.rating = 2 THEN e.base_salary * 0.05
        ELSE 0
    END AS annual_bonus
FROM
    employees e
JOIN
    performance p ON e.employee_id = p.employee_id
WHERE
    p.year = 2023;


