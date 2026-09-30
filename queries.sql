-- ==============================
-- SELECT QUERIES
-- ==============================

-- View all students
SELECT *
FROM students;

-- View students with GPA greater than 3.0
SELECT *
FROM students
WHERE gpa > 3.0;

-- View students from Lahore
SELECT *
FROM students
WHERE city = 'Lahore';


-- ==============================
-- UPDATE QUERY
-- ==============================

-- Update a student's GPA
UPDATE students
SET gpa = 3.75
WHERE student_id = 1;


-- ==============================
-- DELETE QUERY
-- ==============================

-- Delete a student
DELETE FROM students
WHERE student_id = 1;