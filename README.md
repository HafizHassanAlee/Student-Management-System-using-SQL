# Student Management System

A simple **Student Management System** built with **Python** and **PostgreSQL**.

This project was created to practice connecting Python with a real PostgreSQL database and implementing the four basic **CRUD operations**:

* **Create** — Add a new student
* **Read** — View student records
* **Update** — Modify an existing student
* **Delete** — Remove a student

---

## 🚀 Features

* Add new student records
* Display all students
* Update student information
* Delete student records
* Student ID-based record management
* Input validation for:

  * Name
  * Age
  * City
  * Major
  * GPA
* GPA validation from **0.0 to 4.0**
* PostgreSQL database storage
* Menu-driven command-line interface
* Uses parameterized SQL queries

---

## 🛠️ Technologies Used

* **Python**
* **PostgreSQL**
* **Psycopg 3**
* SQL
* Git & GitHub

---

## 📂 Project Structure

```text
STUDENT-MANAGEMENT-SYSTEM/
│
├── sqlpracticepostgres.py
└── README.md
```

---

## 🗄️ Database Structure

The project uses a PostgreSQL database named:

```text
students_database
```

The main table is:

```sql
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    city VARCHAR(100),
    major VARCHAR(100),
    gpa DECIMAL(3,2)
);
```

### Table Columns

| Column       | Data Type | Description       |
| ------------ | --------- | ----------------- |
| `student_id` | SERIAL    | Unique student ID |
| `name`       | VARCHAR   | Student name      |
| `age`        | INTEGER   | Student age       |
| `city`       | VARCHAR   | Student city      |
| `major`      | VARCHAR   | Student major     |
| `gpa`        | DECIMAL   | Student GPA       |

---

## 🔄 CRUD Operations

### 1. Create

Adds a new student to the PostgreSQL database.

```sql
INSERT INTO students
(name, age, city, major, gpa)
VALUES
(%s, %s, %s, %s, %s);
```

### 2. Read

Retrieves all students from the database.

```sql
SELECT student_id, name, age, city, major, gpa
FROM students
ORDER BY student_id;
```

### 3. Update

Updates an existing student's information using their student ID.

```sql
UPDATE students
SET name = %s,
    age = %s,
    city = %s,
    major = %s,
    gpa = %s
WHERE student_id = %s;
```

### 4. Delete

Deletes a student using their student ID.

```sql
DELETE FROM students
WHERE student_id = %s;
```

---

## 📦 Installation

### 1. Install Python

Make sure Python is installed on your computer.

Check your Python version:

```bash
python --version
```

### 2. Install PostgreSQL

Install PostgreSQL and make sure the PostgreSQL server is running.

### 3. Install Psycopg

Install the PostgreSQL adapter for Python:

```bash
pip install psycopg
```

### 4. Create the Database

Create a PostgreSQL database named:

```text
students_database
```

Then create the `students` table using the SQL shown above.

---

## 🔐 Database Connection

The Python program connects to PostgreSQL using Psycopg:

```python
import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="students_database",
    user="postgres",
    password="YOUR_PASSWORD",
    port=5432
)
```

**Do not upload your real database password to GitHub.**

For a real project, store credentials in environment variables or a `.env` file and add the `.env` file to `.gitignore`.

---

## ▶️ How to Run

Open the project folder in VS Code or PowerShell.

Run:

```bash
python sqlpracticepostgres.py
```

The program will display:

```text
====== STUDENT MANAGEMENT SYSTEM ======
1. Create Student
2. Read Students
3. Update Student
4. Delete Student
5. Exit
```

Enter a number to perform the desired operation.

---

## 💻 Example

### Adding a Student

```text
Enter your choice: 1

Enter student name: Ahmed Ali
Enter age: 20
Enter city: Lahore
Enter major: Computer Science
Enter GPA: 3.5

Student added successfully.
```

### Viewing Students

```text
--------- STUDENTS ---------

ID: 1 | Name: Ahmed Ali | Age: 20 | City: Lahore | Major: Computer Science | GPA: 3.50
```

---

## 🧠 What I Practiced

This project helped me practice:

* Python functions
* `while` loops
* Conditional statements
* Input validation
* Lists and tuples
* PostgreSQL
* SQL queries
* `INSERT`
* `SELECT`
* `UPDATE`
* `DELETE`
* SQL `WHERE`
* `ORDER BY`
* Database connections
* Python database cursors
* `fetchall()`
* `cursor.rowcount`
* `commit()`
* Parameterized SQL queries
* Git and GitHub

---

## 📚 Learning Purpose

This is a **learning project** created to gain practical experience with Python, SQL, PostgreSQL, and database-driven applications.

It is a command-line application and is intentionally kept simple so that the core Python and database concepts are easy to understand.

---

## 🔮 Future Improvements

Possible improvements include:

* Search students
* Filter students by major
* Filter students by GPA
* Sort students
* Add email and phone number
* Add authentication
* Add a graphical interface
* Build a web version
* Connect the project to an API
* Add better error handling
* Use environment variables for database credentials

---

## 👨‍💻 Author

**Hassan Ali**

Learning Python, SQL, PostgreSQL, Git, GitHub, and software development.

---

## ⭐ Project Status

**Completed — Learning Project**

More features and improvements can be added as my programming and database skills grow.
