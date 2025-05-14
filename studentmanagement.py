import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",  # change this
        database="student_db"
    )

def add_student(roll_no, name, age, course, email):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO students (roll_no, name, age, course, email) VALUES (%s, %s, %s, %s, %s)"
    values = (roll_no, name, age, course, email)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    print("Student added successfully.")

def view_students():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    for row in result:
        print(row)
    conn.close()

def search_student(roll_no):
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT * FROM students WHERE roll_no = %s"
    cursor.execute(query, (roll_no,))
    result = cursor.fetchone()
    print(result)
    conn.close()

def update_student(roll_no, name, age, course, email):
    conn = connect()
    cursor = conn.cursor()
    query = "UPDATE students SET name=%s, age=%s, course=%s, email=%s WHERE roll_no=%s"
    values = (name, age, course, email, roll_no)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    print("Student updated successfully.")

def delete_student(roll_no):
    conn = connect()
    cursor = conn.cursor()
    query = "DELETE FROM students WHERE roll_no=%s"
    cursor.execute(query, (roll_no,))
    conn.commit()
    conn.close()
    print("Student deleted successfully.")

def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            roll_no = int(input("Roll No: "))
            name = input("Name: ")
            age = int(input("Age: "))
            course = input("Course: ")
            email = input("Email: ")
            add_student(roll_no, name, age, course, email)

        elif choice == '2':
            view_students()

        elif choice == '3':
            roll_no = int(input("Enter Roll No to search: "))
            search_student(roll_no)

        elif choice == '4':
            roll_no = int(input("Roll No: "))
            name = input("New Name: ")
            age = int(input("New Age: "))
            course = input("New Course: ")
            email = input("New Email: ")
            update_student(roll_no, name, age, course, email)

        elif choice == '5':
            roll_no = int(input("Enter Roll No to delete: "))
            delete_student(roll_no)

        elif choice == '6':
            break

        else:
            print("Invalid choice. Try again.")

menu()
