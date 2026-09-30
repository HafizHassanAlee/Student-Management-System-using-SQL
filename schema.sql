CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    city VARCHAR(100),
    major VARCHAR(100),
    gpa DECIMAL(3,2)
);