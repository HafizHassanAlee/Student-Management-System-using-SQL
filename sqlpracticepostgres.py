import psycopg

# ---------------- DATABASE CONNECTION ----------------

conn = psycopg.connect(
    host="localhost",
    dbname="students_database",
    user="postgres",
    password="hassan92786",
    port=5432
)

cursor = conn.cursor()

# ================= INPUT FUNCTIONS =================

def check_int(int_no):
    while True:
        inp = input(int_no).strip()
        if inp.isdigit():
            inp = int(inp)
            return inp
            break
        else:
            print("ENTER VALID NUMBER..")

def check_string(string_inp):
    while True:
        inp = input(string_inp).strip()
        if inp.replace(" ", "").isalpha():
            inp = str(inp).title()
            return inp
            break
        else:
            print("ENTER VALID INPUT(NO NUMBERS ALLOWED)..")

def check_gpa(float_inp):
    while True:
        gpa = input(float_inp).strip()
        try:
            gpa = float(gpa)
            if gpa >= 0 and gpa <= 4 :
                return gpa
                break
        except:
            print("ENTER VALID GPA..")

# ================= CRUD FUNCTIONS =================

# CREATE
def create_student():
    name = check_string("Enter student name: ")
    age = check_int("Enter age: ")
    city = check_string("Enter city: ")
    major = check_string("Enter major: ")
    gpa = check_gpa("Enter GPA: ")

    cursor.execute("""
        INSERT INTO students (name, age, city, major, gpa)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, age, city, major, gpa))

    conn.commit()

    print("Student added successfully.")

# READ
def read_students():
    cursor.execute("""
        SELECT student_id, name, age, city, major, gpa
        FROM students
        ORDER BY student_id
    """)

    students = cursor.fetchall()

    if not students:
        print("No students found.")
        return

    print("\n--------- STUDENTS ---------")

    for student in students:
        print(
            f"ID: {student[0]} | "
            f"Name: {student[1]} | "
            f"Age: {student[2]} | "
            f"City: {student[3]} | "
            f"Major: {student[4]} | "
            f"GPA: {student[5]}"
        )

# UPDATE
def update_student():
    cursor.execute("""SELECT student_id FROM students""")
    all_ids = [row[0] for row in cursor.fetchall()]

    student_id = check_int("Enter student ID to update: ")

    if student_id not in all_ids:
        print("STUDENT NOT FOUND..")
        return

    cursor.execute("""
        SELECT * FROM students
        WHERE student_id = %s"""
        ,(student_id,))

    x = cursor.fetchall()
    for student in x:
        print(
         f"ID   :   {student[0]} \n"
         f"Name :   {student[1]} \n"
         f"Age  :   {student[2]} \n"
         f"City :   {student[3]} \n"
         f"Major:   {student[4]} \n"
         f"GPA  :   {student[5]}"
    )

    print("PREVIOUS STORED VALUES ARE GIVEN UPPER..\nENTER NEW VALUES TO ADD:")

    name = check_string("Enter new name: ")
    age = check_int("Enter new age: ")
    city = check_string("Enter new city: ")
    major = check_string("Enter new major: ")
    gpa = check_gpa(input("Enter new GPA: "))

    cursor.execute("""
        UPDATE students
        SET name = %s,
            age = %s,
            city = %s,
            major = %s,
            gpa = %s
        WHERE student_id = %s
    """, (name, age, city, major, gpa, student_id))

    conn.commit()

    if cursor.rowcount == 0:
        print("Student not found.")
    else:
        print("Student updated successfully.")

# DELETE
def delete_student():
    student_id = check_int("Enter student ID to delete: ")

    cursor.execute("""
        DELETE FROM students
        WHERE student_id = %s
    """, (student_id,))

    conn.commit()

    if cursor.rowcount == 0:
        print("Student not found.")
    else:
        print("Student deleted successfully.")

# ================= MENU =================

def main():
    while True:

        print("\n====== STUDENT MANAGEMENT SYSTEM ======")
        print("1. Create Student")
        print("2. Read Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_student()

        elif choice == "2":
            read_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Program closed.")
            break

        else:
            print("Invalid choice.")
        input(f"\nPRESS ENTER TO CONTINUE")

# ================= START PROGRAM =================
if __name__ == "__main__":
    main()

    cursor.close()
    conn.close()