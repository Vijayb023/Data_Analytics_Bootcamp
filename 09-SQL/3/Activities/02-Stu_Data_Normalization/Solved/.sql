CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  last_name VARCHAR NOT NULL,
  first_name VARCHAR NOT NULL
);
CREATE TABLE courses (
  id INTEGER NOT NULL PRIMARY KEY,
  course_name VARCHAR NOT NULL
);
CREATE TABLE student_courses_junction (
  student_id INTEGER NOT NULL,
  FOREIGN KEY (student_id) REFERENCES students(id),
  course_id INTEGER NOT NULL,
  FOREIGN KEY (course_id) REFERENCES courses(id),
  course_term VARCHAR NOT NULL,
  PRIMARY KEY (student_id, course_id)
);
INSERT INTO students (id, last_name, first_name)
VALUES
  (1, 'Skywalker', 'Luke'),
  (2, 'Skywalker', 'Leia'),
  (3, 'Solo', 'Han');

INSERT INTO courses (id, course_name)
VALUES
  (3201, 'Data modeling'),
  (3202, 'Data visualization'),
  (12101, 'Force utilization');

INSERT INTO student_courses_junction (student_id, course_id, course_term)
VALUES
  (1,12101, 'Spring'),
  (1,3201, 'Fall'),
  (1,3202, 'Fall'),
  (2,12101, 'Fall'),
  (2,3202, 'Spring'),
  (3,3201, 'Spring'),
  (3,3202, 'Fall');
-- Query Tables
SELECT * FROM students;

SELECT * FROM courses;

SELECT * FROM student_courses_junction;
SELECT s.id, s.last_name, s.first_name, c.id, c.course_name, j.course_term
FROM students s
LEFT JOIN student_courses_junction j
ON s.id = j.student_id
LEFT JOIN courses c
ON c.id = j.course_id;
