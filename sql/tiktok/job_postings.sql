CREATE TABLE job_postings (
    job_id SERIAL PRIMARY KEY,
    company_name VARCHAR(255),
    job_title VARCHAR(255),
    job_description TEXT
);

INSERT INTO job_postings (company_name, job_title, job_description) VALUES
('Company A', 'Software Engineer', 'Develop and maintain software applications.'),
('Company A', 'Software Engineer', 'Develop and maintain software applications.'),
('Company B', 'Data Scientist', 'Analyze data to gain insights for business.'),
('Company B', 'Data Scientist', 'Analyze data to gain insights for business.'),
('Company C', 'Product Manager', 'Oversee product development lifecycle.'),
('Company D', 'Software Engineer', 'Develop software applications with Python.'),
('Company E', 'Data Analyst', 'Analyze data and generate reports.');

select job_title, job_description,COUNT(*)
from job_postings
GROUP BY job_title, job_description
having COUNT(*)>1