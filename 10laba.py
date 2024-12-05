import sqlite3

conn = sqlite3.connect('collegess.db')  
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS faculties (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birth_date TEXT NOT NULL,
    faculty_id INTEGER NOT NULL,
    FOREIGN KEY (faculty_id) REFERENCES faculties (id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    faculty_id INTEGER NOT NULL,
    FOREIGN KEY (faculty_id) REFERENCES faculties (id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS enrollments (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    grade INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (course_id) REFERENCES courses (id),
    PRIMARY KEY (student_id, course_id)
)
''')

cursor.executemany('''
INSERT INTO faculties (name) VALUES (?)
''', [('Информационные технологии',), ('Механика',), ('Экономика',)])

cursor.execute('SELECT id FROM faculties WHERE name = "Информационные технологии"')
it_faculty_id = cursor.fetchone()[0]

cursor.execute('SELECT id FROM faculties WHERE name = "Механика"')
mechanical_faculty_id = cursor.fetchone()[0]

cursor.execute('SELECT id FROM faculties WHERE name = "Экономика"')
economics_faculty_id = cursor.fetchone()[0]

cursor.executemany('''
INSERT INTO students (name, birth_date, faculty_id)
VALUES (?, ?, ?)
''', [
    ('Власян Артём', '2006-02-15', it_faculty_id),
    ('Зайцев Илья', '2006-06-22', mechanical_faculty_id),
    ('Калентьев Алексей', '2006-09-03', economics_faculty_id),
    ('Зотов Дмитрий', '2006-11-10', it_faculty_id),
])

cursor.executemany('''
INSERT INTO courses (name, faculty_id)
VALUES (?, ?)
''', [
    ('Программирование', it_faculty_id),
    ('Математика', mechanical_faculty_id),
    ('Экономика', economics_faculty_id),
    ('Алгоритмы и структуры данных', it_faculty_id),
])

cursor.execute('DELETE FROM enrollments')

cursor.executemany('''
INSERT OR IGNORE INTO enrollments (student_id, course_id, grade)
VALUES (?, ?, ?)
''', [
    (1, 1, 5),
    (2, 2, 4),
    (3, 3, 5),
    (4, 4, 5),
])

conn.commit()

cursor.execute('''
SELECT DISTINCT students.name, courses.name, enrollments.grade
FROM students
JOIN enrollments ON students.id = enrollments.student_id
JOIN courses ON enrollments.course_id = courses.id
''')

rows = cursor.fetchall()
print("Студенты и их курсы:")
for row in rows:
    print(f"Студент: {row[0]}, Курс: {row[1]}, Оценка: {row[2]}")

cursor.execute('''
SELECT DISTINCT courses.name
FROM courses
JOIN faculties ON courses.faculty_id = faculties.id
WHERE faculties.name = "Информационные технологии"
''')

rows = cursor.fetchall()
print("\nКурсы факультета 'Информационные технологии':")
for row in rows:
    print(f"Курс: {row[0]}")

conn.close()
