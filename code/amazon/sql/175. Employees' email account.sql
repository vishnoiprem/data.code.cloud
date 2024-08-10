
CREATE TABLE employees1 (
    employee_id BIGINT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO employees1 (employee_id, name, department, email) VALUES
(1, 'Alice', 'Engineering', 'alice@company.com'),
(2, 'Bob', 'Engineering', 'bob@company.com'),
(3, 'Charlie', 'HR', 'charlie@company.com'),
(4, 'David', 'Marketing', 'david@company.com'),
(5, 'Eve', 'Engineering', 'eve@company.com');


SELECT
    employee_id,
    name,
    department,
    email
FROM
    employees1;
