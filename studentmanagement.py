
import sqlite3

def create_tables():
    conn = sqlite3.connect('studentrecordsdb')
    cursor = conn.cursor()
    
    # Students table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        dob TEXT,
        email TEXT UNIQUE,
        phone TEXT,
        enrollment_date TEXT
    )
    ''')
    
    # Courses table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT,
        course_description TEXT,
        credits INTEGER
    )
    ''')
    
    # Enrollments table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS enrollments (
        enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        course_id INTEGER,
        enrollment_date TEXT,
        grade TEXT,
        FOREIGN KEY (student_id) REFERENCES students(student_id),
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
    )
    ''')
    
    conn.commit()
    conn.close()
