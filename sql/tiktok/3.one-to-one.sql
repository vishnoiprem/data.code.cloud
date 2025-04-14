

CREATE TABLE Person (
    person_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE Passport (
    passport_id INT PRIMARY KEY,
    person_id INT UNIQUE,
    FOREIGN KEY (person_id) REFERENCES Person(person_id)
);


CREATE TABLE Teacher (
    teacher_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE Class (
    class_id INT PRIMARY KEY,
    class_name VARCHAR(100),
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
);